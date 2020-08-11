
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