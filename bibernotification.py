import instaloader

def main():
  L = instaloader.Instaloader()
  profile = L.from_username(username="realpostillon")
  print("Profile:{profile}".format(profile = profile))

if __name__ == "__main__":
  main()
