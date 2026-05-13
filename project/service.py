from analyze import stats_df

class StatsService : 

    # 통계 조회 서비스
    def stats(self):
        return stats_df.to_dict(orient='records')[0]
    
stats_service = StatsService()