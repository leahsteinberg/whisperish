import acquire_emails
from password import correspondence, password, email_address
from standardize_emails import clean_email
import sample

if __name__ == "__main__":
    emails, names = acquire_emails.fetch_emails(email_address, password, correspondence)
    clean_email('FROM'+correspondence[:correspondence.find('@')]+'.txt', correspondence, email_address)

    clean_email('TO'+correspondence[:correspondence.find('@')]+'.txt', email_address, correspondence)
    emailfile_from = open('texts/cleanfrom'+correspondence[:correspondence.find('@')]+'.txt')
    emailbuffer_from = emailfile_from.read(1000000)
    emailfile_to = open('texts/cleanto'+correspondence[:correspondence.find('@')] +'.txt')
    emailbuffer_to = emailfile_to.read(1000000)

    for i in range(10):
      print names[0][0] + ": "
      sample.get_text(emailbuffer_from)
      print names[1][0] + ": "
      sample.get_text(emailbuffer_to)


