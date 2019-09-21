class RingBuffer:
  def __init__(self, capacity):
    self.capacity = capacity
    self.current = 0
    self.storage = [None]*capacity

  def append(self, item):
    if self.current == len(self.storage):
      self.current = 0
      self.append(item)
    else:
      self.storage[self.current] = item
      self.current += 1

  def get(self):
    ret = []
    for val in self.storage:
      if val is not None:
        ret.append(val)
    return ret


if __name__ == '__main__':
  buffer = RingBuffer(5)
  buffer.append('1')
  buffer.append('2')
  buffer.append('3')
  buffer.append('4')
  buffer.append('5')
    
  buffer.append('6')
  buffer.append('7')
  print(len(buffer.storage))
  print(buffer.get())