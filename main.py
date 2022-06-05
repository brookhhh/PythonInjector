from pymem import *
import time
import os

os.system("Bedrock Injector")
for file_name in os.listdir(os.path):
  os.path.normpath(file_name)
  
  # you know what this is
  if __name__ == '__main__':
    pymem = Pymem()
    print("Opening Minecraft...")
    time.sleep(100)

    # injecting dll
    if pymem.open_process_from_name('Minecraft.Bedrock'):
        print("Injecting...")
        pymem.injectDll(file_name.endswith('.dll') in "\\PythonInjectorMCBE")
        print("Should be injected!")
