import imaplib, email
import password, os


def fetch_emails(user, password, friend):
  mail = imaplib.IMAP4_SSL('imap.gmail.com')
  mail.login(user, password)
  email_files = {}
  names = []
  file_recvd, name_friend  = gather(mail, 'inbox', friend)
  names.append(name_friend)
  email_files['received'] = file_recvd
  file_sent, name_user = gather(mail, '[Gmail]/Sent Mail', friend)
  names.append(name_user)
  email_files['sent'] = file_sent
  return email_files, names


def get_name(message):
  name = message['From']
  name = name[:name.find('<')]
  name = name.translate(None, '"')
  name = name.lower()
  if ',' in name:
    name = name.translate(None, ',')
    name = name.split(' ')
    name_tuple = (name[1], name[0])
  else:
    name = name.split(' ')
    name_tuple = (name[0], name[1])
  return name_tuple



def gather(mail, folder, address):
  mail.list()
  mail.select(folder)
  preposition = '(FROM' if folder == 'inbox' else '(TO'
  string =  preposition + ' "' + address + '"'+ ')'
  result, data = mail.uid('search', None, string)
  if result == 'OK':
    data = data[0].split(' ')
  else:
    print "error"
    return
  name_tuple = ()
  preposition = preposition[1:]
  file_name = preposition + address[:address.find('@')] + '.txt'
  file_d = open("texts/"+file_name, 'w')
  for i in reversed(xrange(len(data))):
    latest_uid = data[i*-1]
    result, e_data = mail.uid('fetch', latest_uid, '(RFC822)')
    raw_email = e_data[0][1]
    message = email.message_from_string(raw_email.decode('utf-8'))
    if i == 0:
      name_tuple = get_name(message)
    for part in message.walk():
      if part.get_content_type() == 'text/plain':
        body = part.get_payload(decode = True)
        file_d.write(body)
  return file_name, name_tuple

if __name__ == '__main__':
  emails = fetch_emails(password.email_address, password.password, password.correspondence)

