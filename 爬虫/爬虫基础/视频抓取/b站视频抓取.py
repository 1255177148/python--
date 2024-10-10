import gevent  # 使用协程，并发提高下载速度
from gevent import monkey

monkey.patch_all()  # 这里使用了monkey
import requests
import copy
from lxml import etree
import re
import json
from jsonpath import jsonpath
from moviepy.editor import ffmpeg_tools  # 这是一个处理音视频剪辑的库


class PullVedio:

    def __init__(self, htmlUrl, cookie) -> None:
        self.htmlUrl = htmlUrl
        self.cookie = cookie
        self.referer = htmlUrl
        self.headers = {
            "Referer": htmlUrl,
            "Cookie": cookie,
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36",
        }

    def getVedioInfo(self):
        """
        抓取b站页面html，获取里面的音视频数据，之后可以根据获取到的数据，提取对应的音视频
        """
        res = requests.get(url=self.htmlUrl, headers=self.headers)
        html = etree.HTML(res.content.decode())
        title_source = html.xpath('/html/head/title/text()') # 获取视频标题
        source_data = html.xpath("/html/head/script[4]/text()") # 获取音视频详细信息
        movie_source = re.search(r"playurlSSRData(.*?)}}}}", source_data[0])
        json_map = {}
        # 将视频标题放入字典
        title = title_source[0].split('_')[0]
        json_map['title'] = title
        if movie_source:
            json_source = movie_source.group()
            json_data = re.sub("playurlSSRData = ", "", json_source, 1)
            json_o = json.loads(json_data)
            # 获取视频信息
            video_url = jsonpath(json_o, "$.result.video_info.dash.video[0].base_url")
            video_size = jsonpath(json_o, "$.result.video_info.dash.video[0].size")
            video_max_range = jsonpath(
                json_o, "$.result.video_info.dash.video[0].SegmentBase.indexRange"
            )
            # 获取音频信息
            audio_url = jsonpath(json_o, "$.result.video_info.dash.audio[0].base_url")
            audio_size = jsonpath(json_o, "$.result.video_info.dash.audio[0].size")
            audio_max_range = jsonpath(
                json_o, "$.result.video_info.dash.audio[0].SegmentBase.indexRange"
            )
            # 组装返回
            json_map["videoUrl"] = video_url[0]
            json_map["videoSize"] = video_size[0]
            json_map["videoRange"] = video_max_range[0].split("-")[1]
            json_map["audioUrl"] = audio_url[0]
            json_map["audioSize"] = audio_size[0]
            json_map["audioRange"] = audio_max_range[0].split("-")[1]
        else:
            json_data = re.sub('window.__playinfo__=','', source_data[0], 1)
            json_o = json.loads(json_data)
            video_url = jsonpath(json_o, '$.data.dash.video[0].base_url')
            video_max_range = jsonpath(json_o, '$.data.dash.video[0].SegmentBase.indexRange')
            audio_url = jsonpath(json_o, '$.data.dash.audio[0].base_url')
            audio_max_range = jsonpath(json_o, '$.data.dash.audio[0].SegmentBase.indexRange')
            # 组装返回
            json_map["videoUrl"] = video_url[0]
            json_map["videoSize"] = None
            json_map["videoRange"] = video_max_range[0].split("-")[1]
            json_map["audioUrl"] = audio_url[0]
            json_map["audioSize"] = None
            json_map["audioRange"] = audio_max_range[0].split("-")[1]
        return json_map

    def downVedio(self, json_map, video_file):
        """
        视频分段下载并写入到文件中，有时候视频太长，所以要分段下载.

        :param dict json_map: 视频信息
        :param str video_file: 下载到本地的文件路径
        """
        # 获取视频长度
        video_content = json_map["videoSize"]  # 视频总长度
        video_length = json_map["videoRange"]  # 每次请求最大的视频长度
        url = json_map["videoUrl"]
        # 分段下载视频
        self.handleRequest(url, video_file, video_content, video_length)

    def downAudio(self, json_map, audio_file):
        """
        分段下载音频信息并写入到文件中

        :param dict json_map: 视频信息
        :param str audio_file: 下载到本地的文件路径
        """
        audio_size = json_map["audioSize"]  # 音频信息大小
        audio_length = json_map["audioRange"]  # 每次请求最大的音频长度
        url = json_map["audioUrl"]
        # 分段下载
        self.handleRequest(url, audio_file, audio_size, audio_length)

    def handleRequest(self, url, file, size, range):
        """
        批量处理音视频下载请求

        Args:
            url (_str_): 请求地址
            file (_str_): 将获取到的数据写入指定文件里
            size (_int_): 音视频数据大小
            range (_int_): 分段下载每次获取到的数据最大容量
        """
        job_list = []
        start_length = 0
        end_length = int(range)
        if size is None:
            # 这时没有得到视频大小信息，先分段请求一次，拿到响应头里的视频大小信息
            header = copy.deepcopy(self.headers)
            header["Range"] = "bytes=" + str(start_length) + "-" + str(end_length)
            res = requests.get(url=url, headers=header)
            content_range = res.headers['Content-Range'].split('/')[1]
            size = content_range
        while True:
            header = copy.deepcopy(self.headers)
            header["Range"] = "bytes=" + str(start_length) + "-" + str(end_length)
            job_list.append(gevent.spawn(self.sendVedioRequest, header, url))
            start_length = end_length + 1
            end_length = end_length + int(range) - 1
            if start_length > int(size):
                break
            if end_length > int(size):
                end_length = int(size)
        gevent.joinall(job_list)
        result_list = [
            job_object.value for job_object in job_list
        ]  # 这里for循环依次获取协程执行的函数返回的结果
        with open(file, "ab") as f:
            for data in result_list:
                f.write(data)

    def sendVedioRequest(self, header, url):
        """
        This function sends a video request with the provided header and URL.

        :param dict header: The `header` parameter in the `sendVedioRequest` function is typically used to
        pass any necessary headers for the HTTP request. Headers can include information such as authentication tokens,
        content type, user-agent, etc. It helps the server understand the type of
        request being made and how to handle it

        :param str url: The `url` parameter in the `sendVedioRequest` function is the URL of the video that
        you want to request. This URL will be used to access and retrieve the video content
        """
        res = requests.get(url=url, headers=header)
        return res.content

    def mergeVideo(self, videoFile, audioFile, mergeFile):
        """
        将音视频文件合并

        Args:
            videoFile (_str_): 视频文件路径
            audioFile (_str_): 音频文件路径
            mergeFile (_str_): 合并后的文件路径
        """
        ffmpeg_tools.ffmpeg_merge_video_audio(videoFile, audioFile, mergeFile)

if __name__ == '__main__':
    html_url = 'https://www.bilibili.com/video/BV1me2TYdEMG/?spm_id_from=333.1007.top_right_bar_window_dynamic.content.click&vd_source=f6a24697d164c409037b4a81d02627ca'
    cookie = "buvid3=6CB1F980-6BAD-0ACF-32B7-C34B32A9604873484infoc; b_nut=1713767873; _uuid=22A81BA2-CBCC-F42B-ECBC-F104A632AC810E76458infoc; buvid_fp=a2f8defe23c38461ac49acbd377e11f7; b-user-id=90f43d8a-d64b-49d8-3ead-3a8b842a8beb; rpdid=|(umkY)RRluY0J'u~kRuumYuu; header_theme_version=CLOSE; enable_web_push=DISABLE; bmg_af_switch=1; bmg_src_def_domain=i1.hdslb.com; SESSDATA=ca608579%2C1744087073%2C35b0e%2Aa1CjCmfqRZeLW8ifKEM40aBJ6BCe7C0IwxP3y5NrMQb_bqvRquJjUVZAhGajoc6D3F34oSVjVmaGdVSWpDYnhsZDV0Nm1VOFlpVEx1c1NQSW1wWENuSTAyUUJQUkRSYnZlTU1kV0s3eXFQV0xaRjQ0ZnBUV0Nia245d0g4dUlhNlZ4NGV6bXNHQmhRIIEC; bili_jct=f0db4bceb51296eac442ae0c42d1a86c; DedeUserID=300238501; DedeUserID__ckMd5=59391fe1737bdf1b; bili_ticket=eyJhbGciOiJIUzI1NiIsImtpZCI6InMwMyIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3Mjg3OTQzMDIsImlhdCI6MTcyODUzNTA0MiwicGx0IjotMX0.mQvSYGOO6FAZRSDT0_eMpFKHvCBV9g-hEwiZHAE1szo; bili_ticket_expires=1728794242; CURRENT_BLACKGAP=0; sid=8go36z7c; CURRENT_FNVAL=4048; VIP_DEFINITION_GUIDE=1; VIP_CONTENT_REMIND=1; buvid4=45559623-15FA-5144-E915-60245B7D03E374897-024042206-lTDs%2BIBTVnhWBxWWPupc1g%3D%3D; home_feed_column=4; browser_resolution=1159-150; bp_t_offset_300238501=986550805320433664; b_lsid=225EC2B8_19275102CBD"
    pullVedio = PullVedio(html_url, cookie)
    json_map = pullVedio.getVedioInfo()
    video_file = 'pullVedio.mp4'
    audio_file = 'pullAudio.mp4'
    merge_file = str(json_map['title']) + '.mp4'
    video_job = gevent.spawn(pullVedio.downVedio, json_map, video_file)
    audio_job = gevent.spawn(pullVedio.downAudio, json_map, audio_file)
    gevent.joinall([video_job, audio_job])
    pullVedio.mergeVideo(video_file, audio_job, merge_file)