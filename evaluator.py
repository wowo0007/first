class Evaluator:

    def __init__(self, AST):
        self.AST = AST

    def run(self, node):
        if isinstance(node, list):
            for n in node:
                for k, v in n.iteritems():
                    self.execute([k, v])
        elif isinstance(node, dict):
            for k, v in node.items():
                self.execute([k, v])

    def execute(self, loc):
        if isinstance(loc[1], list):
            self.run(loc[1])
        elif loc[0] == 'cetak':
            self.echo(loc[1])
        elif loc[0] == 'stop':
            self.stop()
        elif loc[0] == 'ke':
            self.goto(loc[1])

    def goto(self, v):
        for node in self.AST:
            if v in node:
                self.run(node[v])

    def echo(self, v):
        print(v)

    def stop(self):
        quit()

