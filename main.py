import instaloader

ig = instaloader.Instaloader()

username = input("enter target: ")

ig.download_profile(username)