class Counter:
    def __init__(self):
        self.__count = 0
        self.__closed = False
    
    def add(self):
        if self.__closed:
            raise Exception("Сервис не доступен")
        self.__count += 1
    
    def close(self):
        self.__closed = True
    
    def __enter__(self):
        return self
    
    def __exit__(self, exc_type, exc_value, traceback):
        self.close()
    
    def get_count(self):
        return self.__count

try:
    with Counter() as counter:
        counter.add()
        counter.add()
        print("Количество новых животных:", counter.get_count())
except Exception as e:
        print(e)

