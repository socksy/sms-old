import zmq
import sys
import re
#from sqlalchemy.ext.sqlsoup import SqlSoup
import sqlsoup

#switch between current using npcs
npc_ids = [20, 21, 22]
npc_id_in_use = 0
locations = {'fountain':[113, 164], 'buchanan':[245, 150]}

db = sqlsoup.SQLSoup('mysql://cs3099userc:Rm8.EFsr@cs3099userc.host.cs.st-andrews.ac.uk/cs3099userc_db')

paths = db.cs3099_SMSNPCPathNode.all()
port = "56890"
if len(sys.argv) > 1:
    port = sys.argv[1]
    int(port)

context = zmq.Context()
socket = context.socket(zmq.PAIR)
socket.bind("tcp://*:%s" % port)

while True:
    message = socket.recv()
    matchobj  = re.search('from: (.+)\nmessage:\s(.*)', message)
    print message
    phoneno = matchobj.group(1)
    body = matchobj.group(2)
    place_go = [128,128]
    location_message = 'exploring fun opensim times!'
    
    for location in locations:
        if location in body.lower():
            if location == 'buchanan':
                npc_id_in_use = 0
            elif location == 'fountain':
                npc_id_in_use = 1
            place_go = locations[location]
            print location
            print locations[location]
    matchobj2 = re.match('(\d+),(\d+)', body)
    
    #match object
    if matchobj2:
        npc_id_in_use = 2
        place_go[0] = int(matchobj2.groups[1])
        place_go[1] = int(matchobj2.groups[2])

    old_path = db.cs3099_SMSNPCPathNode.filter_by(npc_id=npc_ids[npc_id_in_use])
    [db.delete(x) for x in old_path]
    #db.delete(old_path)
    db.commit()
    db.cs3099_SMSNPCPathNode.insert(npc_id=npc_ids[npc_id_in_use], 
                order=1, pos_x=place_go[0], pos_y=place_go[1],
                say="Hi " + phoneno + "! Have a good day by "+location_message+"!")
    #rp = db.execute('DELETE FROM `cs3099_SMSNPCPathNode` WHERE npc_id=20')
    db.commit()

    print message
