#========================================================not for use

def separator():
  printf("=========================================")
separator()
printf(" ==>  RandomX Mining Presets Wizard <==  ")
separator()
printf("   /===========\                /==\")
printf("   |  [-----]  |                |  |")
printf("   |  |     |  |                |  |                                  |==|")
printf("   |  [-----]  |                |  | /==/                             |==|")
printf("   |  /========/                |  |/  /                                  ")
printf("   |  |            /=========\  |  /  /     /=========\   /========\  |==|")
printf("   |  |            |  /---\  |  |  \  \     |  /---\  |  /    _____/  |  |")
printf("   |  |            |  |   |  |  |  |\  \    |  \---/  |  |   /_____   |  |")
printf("   |  |            |  \---/  |  |  | \  \   |  ______/   |___     /   |  |")
printf("   |==|            \=========/  |  |  \  \  \=========\  \=======/    |==|")
separator()
separator()
printf("What currency do you want to mine? (full name, no spaces) >>> ")
currency = input("")
for file in os.listdir("/Users/darren/Desktop/test"):
  if file.startswith("00 " + currency):
       f = file
