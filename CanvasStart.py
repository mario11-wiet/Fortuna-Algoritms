import tkinter as tkinter
from Voronoi import Voronoi


class MainWindow:
    RADIUS = 3

    LOCK_FLAG = False

    def __init__(self, master):
        self.master = master
        self.master.title("I hate these studies")

        self.frmMain = tkinter.Frame(self.master, relief=tkinter.RAISED, borderwidth=1)
        self.frmMain.pack(fill=tkinter.BOTH, expand=1)

        self.w = tkinter.Canvas(self.frmMain, width=1000, height=1000)
        self.w.config(background='black')
        self.w.bind('<Double-1>', self.onDoubleClick)
        self.w.pack()

        self.frmButton = tkinter.Frame(self.master)
        self.frmButton.pack()

        self.btnCalculate = tkinter.Button(self.frmButton, text='Calculate', width=50, command=self.onClickCalculate)
        self.btnCalculate.pack(side=tkinter.LEFT)

        self.btnClear = tkinter.Button(self.frmButton, text='Clear', width=50, command=self.onClickClear)
        self.btnClear.pack(side=tkinter.LEFT)

    def onClickCalculate(self):
        if not self.LOCK_FLAG:
            self.LOCK_FLAG = True

            pObj = self.w.find_all()
            points = []
            for p in pObj:
                coord = self.w.coords(p)
                points.append((coord[0] + self.RADIUS, coord[1] + self.RADIUS))

            vp = Voronoi(points)
            vp.process()
            lines = vp.get_output()
            self.drawLinesOnCanvas(lines)
            print(lines)

    def onClickClear(self):
        self.LOCK_FLAG = False
        self.w.delete(tkinter.ALL)

    def onDoubleClick(self, event):
        if not self.LOCK_FLAG:
            self.w.create_oval(event.x - self.RADIUS, event.y - self.RADIUS, event.x + self.RADIUS,
                               event.y + self.RADIUS, fill="white")

    def drawLinesOnCanvas(self, lines):
        for l in lines:
            self.w.create_line(l[0], l[1], l[2], l[3], fill='red')


def main():
    root = tkinter.Tk()
    app = MainWindow(root)
    root.mainloop()


if __name__ == '__main__':
    main()