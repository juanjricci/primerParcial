from repository import Repository
from member import Member


class MemberService:

    def add_member(self, member):
        memberKey = -1
        for key in Repository.membersList:
            memberKey = key
        memberKey = memberKey + 1
        Repository.membersList[memberKey] = member.__dict__

    def update_member(self, key, member):
        if key in Repository.membersList.keys():
            Repository.membersList[key] = member.__dict__
        else:
            raise ValueError('No existe legajo')

    def delete_member(self, key):
        if key in Repository.membersList.keys():
            del Repository.membersList[key]
        else:
            raise ValueError('No existe legajo')
