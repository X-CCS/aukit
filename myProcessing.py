
# def run_normalizer():
#     import aukit
#     from aukit.audio_player import play_sound
#     from aukit import audio_normalizer as ano
#     # inpath = r"hello.wav"
#     # outpath = r"./hello_test.wav"
#     inpath = r"提取人声_1.wav"
#     outpath = r"./1_test.wav"
#     # inpath = r"提取人声_2.wav"
#     # inpath = r"提取人声_3.wav"
#     wav, sr = aukit.load_wav(inpath, with_sr=True)
#     out = ano.remove_silence(wav)
#     out = ano.tune_volume(wav, target_dBFS=-10)
#     save_wav(out, outpath, sr)
#     play_sound(out, sr)

# def run_noise_remover():
#     import aukit
#     # inpath = r"hello.wav"
#     inpath = r"1_test.wav"
#     outpath = r"./提取人声_1_test.wav"
#     # wav = aukit.load_wav(inpath)
#     wav, sr = aukit.load_wav(inpath, with_sr=True)
#     out = aukit.remove_noise(wav)
#     save_wav(out, outpath, sr)
#     aukit.play_audio(out)

# def run_editor():
#     import aukit
#     from aukit.audio_player import play_sound, play_audio
#     from aukit import audio_editor as aed
#     # inpath = r"hello.wav"
#     inpath = r"提取人声_1.wav"
#     outpath = r"./提取人声_1_test.wav"
#     wav, sr = aukit.load_wav(inpath, with_sr=True)
#     aud = aed.wav2audiosegment(wav, sr)
#     out = aed.strip_audio(aud)
#     wav = aed.audiosegment2wav(out)

#     out = aed.remove_silence_wave(wav, sr=sr)
#     out = aed.strip_silence_wave(out, sr=sr)
#     save_wav(out, outpath, sr)
#     print(len(wav), len(out))
#     play_audio(out, sr)

"""
inpath 输入处理的音频
outpath 输出处理完的音频
purpose 原声->去噪->声音正则化->去静默
"""
def audio_processing(inpath,outpath):
    import aukit
    from aukit.audio_player import play_sound
    from aukit import audio_normalizer as ano
    from aukit.audio_player import play_sound, play_audio
    from aukit import audio_editor as aed
    from aukit.audio_io import load_wav, save_wav
    """run_noise_remover"""""
    wav, sr = aukit.load_wav(inpath, with_sr=True)
    out = aukit.remove_noise(wav)
    """run_normalizer"""""
    out = ano.remove_silence(wav)
    out = ano.tune_volume(wav, target_dBFS=-10)
    """run_editor"""""
    aud = aed.wav2audiosegment(wav, sr)
    out = aed.strip_audio(aud)
    wav = aed.audiosegment2wav(out)

    out = aed.remove_silence_wave(wav, sr=sr)
    out = aed.strip_silence_wave(out, sr=sr)
    save_wav(out, outpath, sr)  # 保存音频
    # play_sound(out, sr) # 播放音频
    print(len(wav), len(out))
    print("done")
    # return outpath

if __name__=="__main__":
    inpath = r"./提取人声_1.wav"
    outpath = r"./myProcessing_test.wav"
    audio_processing(inpath,outpath)