import instaloader

def main():
  L = instaloader.Instaloader()
  profile = Profile.from_username(L.context, "realpostillon")
  print("Profile:{profile}".format(profile = profile))

if __name__ == "__main__":
  main()
