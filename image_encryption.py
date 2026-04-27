from PIL import Image
import numpy as np 
import os 


def encrypt_image(input_path,key):
	if not os.path.exists(input_path):
		print("[-] File not Found")
		return

	try:	
		image = Image.open(input_path)
	except Exception as e:
		print("[-] Error opening image:", e)
		return

	try:
		image_array=np.array(image).astype(np.int16)
	except Exception as e:
		print("[-] Error processing image:", e)
		return
	
	encrypted_array = image_array ^ key

	filename = os.path.basename(input_path)
	name, ext = os.path.splitext(filename)
	output_path = f"{name}_encrypted{ext}"
	
	try:
		encrypted_image = Image.fromarray(encrypted_array.astype(np.uint8))
		encrypted_image.save(output_path)

	except Exception as e:
		print("[-] Error saving image:", e)
		return
		
	print("[+] Image encrypted and saved as:", output_path) 

def decrypted_image(input_path, key):
	if not os.path.exists(input_path):
		print("[-] File not Found")
		return
	try:
		image = Image.open(input_path)
	except Exception as e:
		print("[-] Error opening image:", e)
		return

	try:
		image_array=np.array(image).astype(np.int16)
	except Exception as e:
		print("[-] Error processing image:", e)
		return

	decrypted_array = image_array ^ key

	filename = os.path.basename(input_path)
	name, ext = os.path.splitext(filename)
	output_path = f"{name}_decrypted{ext}"

	try:
		decrypted_image = Image.fromarray(decrypted_array.astype(np.uint8))
		decrypted_image.save(output_path)

	except Exception as e:
		print("[-] Error saving image:", e)
		return
		

	print("[+] Image decrypted and saved as:", output_path) 

def main():
	try:
		while True:
			print("============ Image Encryption Tool ============")
			print("1. Encrypt image: ")
			print("2. Decrypt image: ")
			print("3. Exit")

			choice=input("Enter your choice (1/2/3): ")

			if choice == "3":
				print("Goodbye!")
				return 

			while True:
				try:
					key=int(input("Enter key(0-255): "))
					if 0<= key <= 255:
						break
					else:
						print("[-] Key must be between 0 and 255")
						
				except:
					print("Invalid Key ")
					continue

			if choice =="1":
				inp= input("Enter Image Path: ").strip()
				encrypt_image(inp, key)

			elif choice =="2":
				inp= input("Enter Image Path: ").strip()
				decrypted_image(inp,key)
	except KeyboardInterrupt:
		print("\n[!] Program interrupted by user. Exiting safely...")
		print("[+] Goodbye!")


if __name__ == "__main__":
    main()

