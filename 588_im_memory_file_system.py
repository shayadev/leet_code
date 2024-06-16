import bisect
import collections

paths = {}
files = {}


class FileSystem:
    def __init__(self):
        self.paths = collections.defaultdict(list)
        self.files = collections.defaultdict(str)

    def ls(self, path: str):
        if path in self.files:
             return [path.split('/')[-1]]
        else:
           return self.paths[path]

    def mkdir(self, path: str):
        directories= path.split('/')
        for i in range(1,len(directories)):
            current= '/'.join(directories[:i]) or '/'
            if current not in self.paths or directories[i] not in self.paths[current]:
                bisect.insort(self.paths[current],directories[i])
    def add_content_to_file(self, file_path, content):
        if file_path not in self.files:
            self.mkdir(file_path)
        self.files[file_path] += content
    def read_content_from_file(self, file_path):
        return self.files[file_path]
