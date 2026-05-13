import pandas as pd

# 서비스 클래스
class ItemService : 

    # 생성자
    def __init__(self):
        self.df = pd.DataFrame([
            {'id' : 1 , 'name' : '콜라' , 'price' : 1000},
            {'id' : 2, 'name' : '사이다' , 'price' : 2000}])
        
    # 함수
    # 개별조회 서비스
    def item(self , id):
        result = self.df[self.df['id'] == id]
        if result.empty : 
            return "해당 상품이 없습니다"
            # df타입 대신에 .to_json() 또는 .to_dict()
        return result.to_dict(orient = 'records')[0]
    
    # 전체조회 서비스
    def items(self):
        return self.df.to_dict(orient='records')

    # 저장 서비스
    def save(self , item):
        # 저장할 객체를 데이터 프레임으로 만든다
        saveDf = pd.DataFrame([item])
        # 기존 데이터프레임에 새로운 데이터프레임 연결한다.
        self.df = pd.concat([self.df , saveDf] , ignore_index=True)
        return True
    
    # 수정 서비스
    def update(self, item):
        # 수정할 id df에 존재 여부
        update_id = item.get('id')
        if update_id not in self.df['id'].values : 
            return '수정할 상품이 없습니다'
        # 2.  id의 인덱스 찾기 
        idx = self.df[self.df['id'] == update_id].index      
        # 3. 찾은 index에 값 수정
        self.df.loc[idx , item.keys()] = item.values()     
        # 4. 
        return True
    
    def delete(self , id):
        # 삭제할 id df에 존재 여부
        if id not in self.df['id'].values :
            return "삭제할 상품이 없습니다"
        # 삭제할 id 제외한 df 재구성
        self.df = self.df[self.df['id'] != id]
        # 3.
        return True

  # 서비스 객체 생성
item_service = ItemService()      





