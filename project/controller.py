from fastapi import APIRouter
router1 = APIRouter(prefix="/api")

from service import stats_service

# 통계 데이터 조회
@router1.get("/stats")
async def stats():
    return stats_service.stats()