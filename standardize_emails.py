from password import email_address, correspondence


def clean_email(filename, sender, receiver):
  new_file = open('texts/clean' + filename, 'w+')
  with open('texts/'+filename) as text:
    content = text.readlines()
    for line in content:
      line = line.lower()
      line = line.translate(None, ')(:]["?!$~')
      if sender[0] + ' ' + sender[1] in line:
        pass
      elif '>' in line or len(line)<3:
	pass
      elif sender[1] + ', ' + sender[0] in line or sender[0] + ' ' + sender[1] in line or sender[1] + ' ' +sender[0] in line:
        pass
      elif receiver[1] + ', ' + receiver[0] in line or receiver[0] + ' ' + receiver[1] in line:
        pass
      elif '|' in line or '--\n' in line:
	pass
      elif email_address in line or correspondence in line or 'http' in line:
        pass
      else:
        line = line.translate(None, '.,')
        new_file.write(line)
    new_file.close()

