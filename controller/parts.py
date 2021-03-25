from flask import jsonify
from model.parts import PartsDAO

class BaseParts:
    def getAllPartsOld(self):
        D1 = {"pid" : 1, "pname": "Tuerka", "pmaterial" : "steel", "pcolor" : "grey", "pprice" : 2.5}
        D2 = {"pid" : 2, "pname": "Motor", "pmaterial" : "aluminum", "pcolor" : "black", "pprice" : 5000}
        D3 = {"pid" : 3, "pname": "Panel", "pmaterial" : "madera", "pcolor" : "beige", "pprice" : 10}
        result = [D1, D2, D3]
        return jsonify(result)
        #return "All Parts Method"

    def build_map_dict(self, row):
        result = {}
        result['pid'] = row[0]
        result['pname'] = row[1]
        result['pmaterial'] = row[2]
        result['pcolor'] = row[3]
        result['pweight'] = row[4]
        result['pprice'] = row[5]
        return result

    def build_attr_dict(self, pid,pname, pcolor, pmaterial, pprice, pweight):
        result = {}
        result['pid'] = pid
        result['pname'] = pname
        result['pmaterial'] = pmaterial
        result['pcolor'] = pcolor
        result['pweight'] = pweight
        result['pprice'] = pprice
        return result

    def getAllParts(self):
        dao = PartsDAO()
        part_list = dao.getAllParts()
        result_list = []
        for row in part_list:
            obj = self.build_map_dict(row)
            result_list.append(obj)
        return jsonify(result_list)

    def getPartById(self, pid):
        dao = PartsDAO()
        part_tuple = dao.getPartById(pid)
        if not part_tuple:
            return jsonify("Not Found"), 404
        else:
            result = self.build_map_dict(part_tuple)
            return jsonify(result), 200

    def addNewPart(self, json):
        pname = json['pname']
        pcolor = json['pcolor']
        pmaterial = json['pmaterial']
        pprice = json['pprice']
        pweight = json['pweight']
        dao = PartsDAO()
        pid = dao.insertPart(pname, pcolor, pmaterial, pprice, pweight)
        result = self.build_attr_dict(pid,pname, pcolor, pmaterial, pprice, pweight)
        return jsonify(result), 201

    def updatePart(self, json):
        pname = json['pname']
        pcolor = json['pcolor']
        pmaterial = json['pmaterial']
        pprice = json['pprice']
        pweight = json['pweight']
        pid = json['pid']
        dao = PartsDAO()
        updated_code = dao.updatePart(pid, pname, pcolor, pmaterial, pprice, pweight)
        result = self.build_attr_dict(pid,pname, pcolor, pmaterial, pprice, pweight)
        return jsonify(result), 200

    def deletePart(self, pid):
        dao = PartsDAO()
        result = dao.deletePart(pid)
        if result:
            return jsonify("DELETED"), 200
        else:
            return jsonify("NOT FOUND"), 404