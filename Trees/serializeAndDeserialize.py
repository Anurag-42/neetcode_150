class Codec:
    def serialize(self, root):
        if root is None:
            return '&'
        return str(root.val) + ',' + self.serialize(root.left) + ',' + self.serialize(root.right)

    def deserialize(self, data):
        vals = data.split(',')
        self.i = 0

        def build():
            val = vals[self.i]
            self.i += 1
            if val == '&':
                return None
            node = TreeNode(int(val))
            node.left = build()
            node.right = build()
            return node

        return build()
