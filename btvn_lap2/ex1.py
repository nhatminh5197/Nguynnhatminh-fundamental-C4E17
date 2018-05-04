from youtube_dl import YoutubeDL
#Sample 1 : Download a single youtube video
dl = YoutubeDL()
dl.download(['https://www.youtube.com/watch?v=-Z--baP_EZ4&list=PLFMKeQO-z8sOqVoeV0vPc98XzGJMm5I7l'])
Sample 2 : Download mutiple youtube video
dl = YoutubeDL()
dl.download(['https://www.youtube.com/watch?v=lXOUdUs6MpE&index=96&list=PLFMKeQO-z8sOSde4UQvB1GKiXyN15bBO4','https://www.youtube.com/watch?v=im6JT2H2500&index=3&list=PLs-4Ylg1MSNgqefELX4O7JnP32s1mn4HR'])
#Sample 3 : Download audio
option = {
# Tell the downloader to download only the best quality of audio
'format': 'bestaudio/audio'

}
dl = YoutubeDL(options)
dl.download(['https://www.youtube.com/watch?v=c3jHlYsnEe0'])
#sample 4
option = {
#tell downloader to search instead of directly downloading
'defaut_search': 'ytsearch',
# Tell downloader to download only the first entry (vdieo)
'max_downloads':1
}
dl = YoutubeDL(options)
dl.download(['con điên TAMKA PKL'])
#Sample 5 : search and the download the first audio
options = {
    'default_search': 'ytsearch',
    'max_downloads': 1,
    'format': 'bestaudio/audio'
}
dl = YoutubeDL(options)
dl.download(['Nhớ mưa sài gòn lam trường'])
