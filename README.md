# SECURE_UR_FILE

This is a desktop application that enables users to securely save their files in an encrypted format on their local storage. The application uses a two-step authentication process. The first step involves the user entering their username and password, which are stored in an SQLite database. The password is hashed using the MD5 Hash algorithm to enhance security. The second step involves the user's face recognition, which provides an additional layer of authentication.

After successful authentication, the user is granted access to the operations page where they can perform encryption and decryption operations. These operations are performed using a unique key that is specific to the user, making it impossible for anyone else to decrypt the files. This ensures that the user's files are secure and can only be accessed by the user.

To further enhance security, all decrypted files are automatically deleted once the user logs out or closes the application. This feature ensures that the user's files are not left vulnerable and are always kept secure.
