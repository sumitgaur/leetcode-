"""
Core models

EmailMessage(normalized)


EmailProvider (interface)
  - GmailEmailProvider
  - OutlookEmailProvider


CommunicationImportEngine

ImportRequest
"""

from abc import ABC, abstractmethod


class EmailMessage:
    def __init__(self):
        id_: str
        from_addres: str
        to_address: str
        subject: str
        body: str
        sent_at: str


class EmailProvider(ABC):

    @abstractmethod
    def fetchEmail(self, api_token: str, mailbox: str, start_date: datetime, end_date: datetime) -> List[EmailMessage]:
        pass

    @abstractmethod
    def fetchCalendarEvent():

    @abstractmethod
    def normailze():
        pass


class GmailEmailProvider(EmailProvider):
    def __init__(lib_path):
        self.sdk = init_lib(lib_path)

    def fetchEmail(api_token, mailbox, start_date, end_date):
        raw_message = self.sdk.fetch(api_token, mailbox, start_date, end_date)
        raw_message = [{
                           'message': <>,
                       ...
                       .,..

        }]
        # transform  or normailze

        # Emailmessage  objects

        return EmailMessage()

    def normailze(self):
        ...

    def fetchCalendarEvent():
        pass


class OutlookEmailProvider(EmailProvider):
    def __init__(lib_path):
        self.sdk = init_lib(lib_path)

    def fetchEmail(api_token, mailbox, start_date, end_date):
        raw_message = self.sdk.fetch(api_token, mailbox, start_date, end_date)
        raw_message = [{
                           'message': <>,
                       ...
                       .,..

        }]
        # transform  or normailze

        # Emailmessage  objects

        return EmailMessage()

    def normailze(self):
        ...


# CoC
class CommunicationImportEngine:
    def __init__(providers: List[EmailProvider]):
        self.providers = providers  ## lazy loading

    def fetchData(email):
        for provider in self.providers:  ## chain of responsibility
            provider.fetchEmail

    def fetchCalender(outlook=True, gmail=True):
        if outlook:
            self.provider.  ## outlook provide
        elif gmail:
            self.provide  ## gmail






