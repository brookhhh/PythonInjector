from pymem import *
import time
import os

os.system("Bedrock Injector")
for file_name in os.listdir(os.path):

  if __name__ == '__main__':
    pymem = Pymem()
    print("Opening Minecraft...")
    time.sleep(100)
    if pymem.open_process_from_name('Minecraft.Bedrock'):
        print("Injecting...")
        if pymem.injectDll(file_name.endswith('.dll')):
            print("Should be injected!")

