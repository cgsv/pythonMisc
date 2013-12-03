#import os; os.chdir("D:\myfiles\document\upload\MpegWriter1"); ts = TsFile("fw.ts")

class TsParser:

    #buf should be the ts header
    @staticmethod
    def getPID(buf):
        return (ord(buf[1]) & 0x1F) << 8 | ord(buf[2])

    @staticmethod
    def hexp(buf):
        return [hex(ord(m)) for m in buf]

class TsFile:
    
    def __init__(self, filename):
        self.f = open(filename, "rb")

    def getOnePacket(self):
        return self.f.read(188)

    def getPacketByPid(self, pid):
        buf = self.f.read(188)
        while len(buf) == 188:
            if TsParser.getPID(buf) == pid: return buf
            buf = self.f.read(188)

    def moveBackOneP(self):
        self.f.seek(-188, 1)

    def moveForwardOneP(self):
        self.f.seek(188, 1)

    def moveToStart(self):
        self.f.seek(0)

    def moveToEnd(self):
        self.f.seek(0,2)

    def __del__(self):
        self.f.close()
