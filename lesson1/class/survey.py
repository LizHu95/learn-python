class AnonymousSurvey():
    """收集匿名调查问卷的答案"""
    def __init__(self,question):
        """存储一个文件，并未存储答案做准备"""
        self.question=question
        self.response=[]
    def show_question(self):
        """显示调查问卷"""
        print(self.question)
    def store_response(self,new_response):
        """存储单份调查答卷"""
        self.response.append(new_response)
    def show_result(self):
        """显示收集到的所有答卷"""
        print("Survery result:")
        for response in self.response:
            print("-",response)
        