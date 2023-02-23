# Python Libraries / Librerías Python
from Cryptodome.Cipher import AES
from datetime          import datetime
from hashlib           import sha256
from hashlib           import sha512
import base64


# Application Libraries / Librerías de la Aplicación
from utils import EnvVar


# Preconditions / Precondiciones


class Encryption () :

  @staticmethod
  def base64Encode ( string : str ) -> str :
    stringToHashing = string
    stringBytes     = stringToHashing.encode ( 'utf-8' )
    base64Bytes     = base64.b64encode ( stringBytes )
    stringBase64    = base64Bytes.decode ( 'utf-8' )
    return stringBase64

  @staticmethod
  def base64Decode ( string : str ) -> str :
    stringToHashing = string
    stringBytes     = stringToHashing.encode ( 'utf-8' )
    base64Bytes     = base64.b64decode ( stringBytes )
    stringBase64    = base64Bytes.decode ( 'utf-8' )
    return stringBase64

  @staticmethod
  def decrypt ( key, str_byte ) -> bytes :
    data       = base64.b64decode ( str_byte.encode () )
    nonce      = data [ 0 : 8 ] + data [ 16 : 24 ]
    tag        = data [ 8 : 16 ] + data [ 24 : 32 ]
    ciphertext = data [ AES.block_size * 2 : ]
    cipher     = AES.new ( key, AES.MODE_EAX, nonce )
    return cipher.decrypt_and_verify ( ciphertext, tag )

  @staticmethod
  def encrypt ( key, data ) -> str :
    cipher          = AES.new ( key, AES.MODE_EAX )
    ciphertext, tag = cipher.encrypt_and_digest ( data )
    str_byte        = cipher.nonce [ 0 : 8 ] + tag [ 0 : 8 ] + cipher.nonce [ 8 : 16 ] + tag [ 8 : 16 ] + ciphertext
    return base64.b64encode ( str_byte ).decode ()

  @staticmethod
  def generateHash ( emailToHashing ) -> str :
    salt              = 'QweRt1!2"3#4$5%AsDF'
    dateNow           = datetime.now ()
    formatDate        = dateNow.strftime ( '%d%m%Y%H' )
    emailBase64Encode = Encryption.base64Encode ( emailToHashing )
    saltedInputString = salt + emailBase64Encode + formatDate
    valueHash         = sha256 ( saltedInputString.encode () ).hexdigest ()
    return valueHash

  @staticmethod
  def password ( password : str ) -> str :
    #salt = '842d76ade9070cb1ba2577cfa7bfd18b8a40c173'
    salt      = EnvVar.get ( 'SECRET_KEY' )
    loginHash = ''
    inputData = salt + password
    loginHash = sha512 ( inputData.encode () ).hexdigest ()
    return loginHash
