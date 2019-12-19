import os
import random


music_folder = 'home/valeriy/programs/Music/'
music = ['music1', 'music2', 'music3', 'music4']
random_music = music_folder + random.choice(music) + '.mp3'
os.system(random_music)


