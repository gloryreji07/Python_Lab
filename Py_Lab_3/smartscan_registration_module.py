import cv2
import qrcode

# In-Memory Storage
users_db = []


def in_memory():
    # Lambda functions
    create = lambda name, email, gender: {
        "name": name,
        "email": email,
        "gender": gender,
    }
    insert = lambda user: users_db.append(user)
    fetch = lambda: users_db
    return create, insert, fetch


# SmartScan Code Generation


def generate_smartscan(name, email, gender, filename):
    img = qrcode.make(f"{name},{email},{gender}")
    img.save(f"{filename}.png")
    print(f"QR code saved to file: {filename}.png")


# SmartScan Code Decoding
def decode_smartscan(path):
    image = cv2.imread(f"{path}.png")
    qrCodeDetector = cv2.QRCodeDetector()
    decodedText, points, _ = qrCodeDetector.detectAndDecode(image)
    if points is not None:
        # QR Code detected handling code
        print("QR code detected")
        return decodedText

    else:
        print("QR code not detected")
        return None


# Decode User Data
def decode_smartscan_code(code):
    name, email, gender = code.split(",")
    return {"name": name, "email": email, "gender": gender}


# User Registration Function
def RegisterUserFromSmartScan(path, create, insert, fetch):
    # Decode the SmartScan Code
    decoded_data = decode_smartscan(path)
    if not decoded_data:
        print("No user data found in the SmartScan code.")
        return

    # Extract user data from the decoded SmartScan code
    user_data = decode_smartscan_code(decoded_data)
    name = user_data["name"]
    email = user_data["email"]
    gender = user_data["gender"]

    # Create a new user record
    new_user = create(name, email, gender)

    # Insert the user record into the in-memory list
    insert(new_user)
