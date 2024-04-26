def solution(id_pw, db):
    uid, upw = id_pw
    for i in db:
        dbid,dbpw = i
        
        if uid == dbid:
            if upw == dbpw:
                return "login"
            else:
                return 'wrong pw'
    return 'fail'