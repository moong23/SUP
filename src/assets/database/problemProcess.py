import json
from typing import List, Dict

data = {
  "1864": {
    "problemId": "1864",
    "problemLevel": 4,
    "problemName": "문어 숫자",
    "average_try": 1.3983,
    "solvedtags": [
      {
        "bojTagId": 121,
        "key": "arithmetic"
      },
      {
        "bojTagId": 102,
        "key": "implementation"
      },
      {
        "bojTagId": 124,
        "key": "math"
      },
      {
        "bojTagId": 158,
        "key": "string"
      }
    ],
    "lastupdate": 1687116854.132675
  },
  "9548": {
    "problemId": "9548",
    "problemLevel": 20,
    "problemName": "무제",
    "average_try": 2.25,
    "solvedtags": [
      {
        "bojTagId": 175,
        "key": "data_structures"
      },
      {
        "bojTagId": 159,
        "key": "rope"
      },
      {
        "bojTagId": 69,
        "key": "splay_tree"
      },
      {
        "bojTagId": 158,
        "key": "string"
      },
      {
        "bojTagId": 120,
        "key": "trees"
      }
    ],
    "lastupdate": 1687116854.132885
  },
  "15649": {
    "problemId": "15649",
    "problemLevel": 8,
    "problemName": "N과 M (1)",
    "average_try": 1.6014,
    "solvedtags": [
      {
        "bojTagId": 5,
        "key": "backtracking"
      }
    ],
    "lastupdate": 1687116861.566049
  },
  "15650": {
    "problemId": "15650",
    "problemLevel": 8,
    "problemName": "N과 M (2)",
    "average_try": 1.3524,
    "solvedtags": [
      {
        "bojTagId": 5,
        "key": "backtracking"
      }
    ],
    "lastupdate": 1687116861.566093
  },
  "15651": {
    "problemId": "15651",
    "problemLevel": 8,
    "problemName": "N과 M (3)",
    "average_try": 1.4973,
    "solvedtags": [
      {
        "bojTagId": 5,
        "key": "backtracking"
      }
    ],
    "lastupdate": 1687116861.566124
  },
  "15652": {
    "problemId": "15652",
    "problemLevel": 8,
    "problemName": "N과 M (4)",
    "average_try": 1.2704,
    "solvedtags": [
      {
        "bojTagId": 5,
        "key": "backtracking"
      }
    ],
    "lastupdate": 1687116861.566151
  },
  "15654": {
    "problemId": "15654",
    "problemLevel": 8,
    "problemName": "N과 M (5)",
    "average_try": 1.3739,
    "solvedtags": [
      {
        "bojTagId": 5,
        "key": "backtracking"
      }
    ],
    "lastupdate": 1687116861.566174
  },
  "15655": {
    "problemId": "15655",
    "problemLevel": 8,
    "problemName": "N과 M (6)",
    "average_try": 1.1779,
    "solvedtags": [
      {
        "bojTagId": 5,
        "key": "backtracking"
      }
    ],
    "lastupdate": 1687116861.566198
  },
  "15656": {
    "problemId": "15656",
    "problemLevel": 8,
    "problemName": "N과 M (7)",
    "average_try": 1.2681,
    "solvedtags": [
      {
        "bojTagId": 5,
        "key": "backtracking"
      }
    ],
    "lastupdate": 1687116861.566219
  },
  "15657": {
    "problemId": "15657",
    "problemLevel": 8,
    "problemName": "N과 M (8)",
    "average_try": 1.2213,
    "solvedtags": [
      {
        "bojTagId": 5,
        "key": "backtracking"
      }
    ],
    "lastupdate": 1687116861.566251
  },
  "15663": {
    "problemId": "15663",
    "problemLevel": 9,
    "problemName": "N과 M (9)",
    "average_try": 2.0339,
    "solvedtags": [
      {
        "bojTagId": 5,
        "key": "backtracking"
      }
    ],
    "lastupdate": 1687116861.56628
  },
  "15664": {
    "problemId": "15664",
    "problemLevel": 9,
    "problemName": "N과 M (10)",
    "average_try": 1.236,
    "solvedtags": [
      {
        "bojTagId": 5,
        "key": "backtracking"
      }
    ],
    "lastupdate": 1687116861.566302
  },
  "15665": {
    "problemId": "15665",
    "problemLevel": 9,
    "problemName": "N과 M (11)",
    "average_try": 1.3033,
    "solvedtags": [
      {
        "bojTagId": 5,
        "key": "backtracking"
      }
    ],
    "lastupdate": 1687116861.566323
  },
  "15666": {
    "problemId": "15666",
    "problemLevel": 9,
    "problemName": "N과 M (12)",
    "average_try": 1.2381,
    "solvedtags": [
      {
        "bojTagId": 5,
        "key": "backtracking"
      }
    ],
    "lastupdate": 1687116861.566342
  },
  "14889": {
    "problemId": "14889",
    "problemLevel": 9,
    "problemName": "스타트와 링크",
    "average_try": 2.1649,
    "solvedtags": [
      {
        "bojTagId": 5,
        "key": "backtracking"
      },
      {
        "bojTagId": 125,
        "key": "bruteforcing"
      }
    ],
    "lastupdate": 1687116861.566361
  },
  "10974": {
    "problemId": "10974",
    "problemLevel": 8,
    "problemName": "모든 순열",
    "average_try": 1.5567,
    "solvedtags": [
      {
        "bojTagId": 5,
        "key": "backtracking"
      },
      {
        "bojTagId": 125,
        "key": "bruteforcing"
      }
    ],
    "lastupdate": 1687116861.566384
  },
  "15658": {
    "problemId": "15658",
    "problemLevel": 9,
    "problemName": "연산자 끼워넣기 (2)",
    "average_try": 1.9162,
    "solvedtags": [
      {
        "bojTagId": 5,
        "key": "backtracking"
      },
      {
        "bojTagId": 125,
        "key": "bruteforcing"
      }
    ],
    "lastupdate": 1687116861.566403
  },
  "16922": {
    "problemId": "16922",
    "problemLevel": 8,
    "problemName": "로마 숫자 만들기",
    "average_try": 1.8301,
    "solvedtags": [
      {
        "bojTagId": 5,
        "key": "backtracking"
      },
      {
        "bojTagId": 125,
        "key": "bruteforcing"
      },
      {
        "bojTagId": 6,
        "key": "combinatorics"
      },
      {
        "bojTagId": 102,
        "key": "implementation"
      },
      {
        "bojTagId": 124,
        "key": "math"
      }
    ],
    "lastupdate": 1687116861.566421
  },
  "18429": {
    "problemId": "18429",
    "problemLevel": 8,
    "problemName": "근손실",
    "average_try": 1.6192,
    "solvedtags": [
      {
        "bojTagId": 5,
        "key": "backtracking"
      },
      {
        "bojTagId": 125,
        "key": "bruteforcing"
      }
    ],
    "lastupdate": 1687116861.566443
  },
  "1553": {
    "problemId": "1553",
    "problemLevel": 11,
    "problemName": "도미노 찾기",
    "average_try": 1.4951,
    "solvedtags": [
      {
        "bojTagId": 5,
        "key": "backtracking"
      },
      {
        "bojTagId": 102,
        "key": "implementation"
      }
    ],
    "lastupdate": 1687116861.566482
  },
  "20950": {
    "problemId": "20950",
    "problemLevel": 9,
    "problemName": "미술가 미미",
    "average_try": 3.6871,
    "solvedtags": [
      {
        "bojTagId": 5,
        "key": "backtracking"
      },
      {
        "bojTagId": 125,
        "key": "bruteforcing"
      }
    ],
    "lastupdate": 1687116861.566501
  },
  "6603": {
    "problemId": "6603",
    "problemLevel": 9,
    "problemName": "로또",
    "average_try": 1.8032,
    "solvedtags": [
      {
        "bojTagId": 5,
        "key": "backtracking"
      },
      {
        "bojTagId": 6,
        "key": "combinatorics"
      },
      {
        "bojTagId": 124,
        "key": "math"
      },
      {
        "bojTagId": 62,
        "key": "recursion"
      }
    ],
    "lastupdate": 1687116861.566519
  },
  "1182": {
    "problemId": "1182",
    "problemLevel": 9,
    "problemName": "부분수열의 합",
    "average_try": 2.2739,
    "solvedtags": [
      {
        "bojTagId": 5,
        "key": "backtracking"
      },
      {
        "bojTagId": 125,
        "key": "bruteforcing"
      }
    ],
    "lastupdate": 1687116861.566537
  },
  "10819": {
    "problemId": "10819",
    "problemLevel": 9,
    "problemName": "차이를 최대로",
    "average_try": 1.5275,
    "solvedtags": [
      {
        "bojTagId": 5,
        "key": "backtracking"
      },
      {
        "bojTagId": 125,
        "key": "bruteforcing"
      }
    ],
    "lastupdate": 1687116861.566556
  },
  "10971": {
    "problemId": "10971",
    "problemLevel": 9,
    "problemName": "외판원 순회 2",
    "average_try": 2.9572,
    "solvedtags": [
      {
        "bojTagId": 5,
        "key": "backtracking"
      },
      {
        "bojTagId": 125,
        "key": "bruteforcing"
      },
      {
        "bojTagId": 138,
        "key": "tsp"
      }
    ],
    "lastupdate": 1687116861.566574
  },
  "2529": {
    "problemId": "2529",
    "problemLevel": 10,
    "problemName": "부등호",
    "average_try": 1.8212,
    "solvedtags": [
      {
        "bojTagId": 5,
        "key": "backtracking"
      },
      {
        "bojTagId": 125,
        "key": "bruteforcing"
      }
    ],
    "lastupdate": 1687116861.566592
  },
  "6987": {
    "problemId": "6987",
    "problemLevel": 12,
    "problemName": "월드컵",
    "average_try": 3.3224,
    "solvedtags": [
      {
        "bojTagId": 5,
        "key": "backtracking"
      },
      {
        "bojTagId": 125,
        "key": "bruteforcing"
      }
    ],
    "lastupdate": 1687116861.56661
  },
  "16987": {
    "problemId": "16987",
    "problemLevel": 11,
    "problemName": "계란으로 계란치기",
    "average_try": 1.9299,
    "solvedtags": [
      {
        "bojTagId": 5,
        "key": "backtracking"
      },
      {
        "bojTagId": 125,
        "key": "bruteforcing"
      }
    ],
    "lastupdate": 1687116861.566628
  },
  "19699": {
    "problemId": "19699",
    "problemLevel": 9,
    "problemName": "소-난다!",
    "average_try": 2.555,
    "solvedtags": [
      {
        "bojTagId": 5,
        "key": "backtracking"
      },
      {
        "bojTagId": 125,
        "key": "bruteforcing"
      },
      {
        "bojTagId": 124,
        "key": "math"
      },
      {
        "bojTagId": 95,
        "key": "number_theory"
      },
      {
        "bojTagId": 9,
        "key": "primality_test"
      },
      {
        "bojTagId": 67,
        "key": "sieve"
      }
    ],
    "lastupdate": 1687116861.566646
  },
  "14712": {
    "problemId": "14712",
    "problemLevel": 11,
    "problemName": "넴모넴모 (Easy)",
    "average_try": 1.8356,
    "solvedtags": [
      {
        "bojTagId": 5,
        "key": "backtracking"
      },
      {
        "bojTagId": 125,
        "key": "bruteforcing"
      }
    ],
    "lastupdate": 1687116861.566665
  },
  "14888": {
    "problemId": "14888",
    "problemLevel": 10,
    "problemName": "연산자 끼워넣기",
    "average_try": 2.081,
    "solvedtags": [
      {
        "bojTagId": 5,
        "key": "backtracking"
      },
      {
        "bojTagId": 125,
        "key": "bruteforcing"
      }
    ],
    "lastupdate": 1687116861.566683
  },
  "16198": {
    "problemId": "16198",
    "problemLevel": 10,
    "problemName": "에너지 모으기",
    "average_try": 1.3237,
    "solvedtags": [
      {
        "bojTagId": 5,
        "key": "backtracking"
      },
      {
        "bojTagId": 125,
        "key": "bruteforcing"
      }
    ],
    "lastupdate": 1687116861.566701
  },
  "10597": {
    "problemId": "10597",
    "problemLevel": 10,
    "problemName": "순열장난",
    "average_try": 3.274,
    "solvedtags": [
      {
        "bojTagId": 5,
        "key": "backtracking"
      }
    ],
    "lastupdate": 1687116861.566736
  },
  "1174": {
    "problemId": "1174",
    "problemLevel": 11,
    "problemName": "줄어드는 수",
    "average_try": 2.4035,
    "solvedtags": [
      {
        "bojTagId": 5,
        "key": "backtracking"
      },
      {
        "bojTagId": 125,
        "key": "bruteforcing"
      }
    ],
    "lastupdate": 1687116861.566754
  },
  "1189": {
    "problemId": "1189",
    "problemLevel": 10,
    "problemName": "컴백홈",
    "average_try": 1.8315,
    "solvedtags": [
      {
        "bojTagId": 5,
        "key": "backtracking"
      },
      {
        "bojTagId": 125,
        "key": "bruteforcing"
      },
      {
        "bojTagId": 127,
        "key": "dfs"
      },
      {
        "bojTagId": 7,
        "key": "graphs"
      },
      {
        "bojTagId": 11,
        "key": "graph_traversal"
      }
    ],
    "lastupdate": 1687116861.566773
  },
  "19942": {
    "problemId": "19942",
    "problemLevel": 11,
    "problemName": "다이어트",
    "average_try": 3.9368,
    "solvedtags": [
      {
        "bojTagId": 5,
        "key": "backtracking"
      },
      {
        "bojTagId": 125,
        "key": "bruteforcing"
      }
    ],
    "lastupdate": 1687116861.56679
  },
  "18290": {
    "problemId": "18290",
    "problemLevel": 10,
    "problemName": "NM과 K (1)",
    "average_try": 3.8887,
    "solvedtags": [
      {
        "bojTagId": 5,
        "key": "backtracking"
      },
      {
        "bojTagId": 125,
        "key": "bruteforcing"
      }
    ],
    "lastupdate": 1687116861.566809
  },
  "1497": {
    "problemId": "1497",
    "problemLevel": 9,
    "problemName": "기타콘서트",
    "average_try": 3.257,
    "solvedtags": [
      {
        "bojTagId": 14,
        "key": "bitmask"
      },
      {
        "bojTagId": 125,
        "key": "bruteforcing"
      },
      {
        "bojTagId": 6,
        "key": "combinatorics"
      },
      {
        "bojTagId": 124,
        "key": "math"
      }
    ],
    "lastupdate": 1687116861.566826
  },
  "18430": {
    "problemId": "18430",
    "problemLevel": 12,
    "problemName": "무기 공학",
    "average_try": 2.148,
    "solvedtags": [
      {
        "bojTagId": 5,
        "key": "backtracking"
      }
    ],
    "lastupdate": 1687116861.566844
  },
  "15566": {
    "problemId": "15566",
    "problemLevel": 10,
    "problemName": "개구리 1",
    "average_try": 3.2913,
    "solvedtags": [
      {
        "bojTagId": 5,
        "key": "backtracking"
      },
      {
        "bojTagId": 125,
        "key": "bruteforcing"
      }
    ],
    "lastupdate": 1687116861.566861
  },
  "9663": {
    "problemId": "9663",
    "problemLevel": 12,
    "problemName": "N-Queen",
    "average_try": 2.1409,
    "solvedtags": [
      {
        "bojTagId": 5,
        "key": "backtracking"
      },
      {
        "bojTagId": 125,
        "key": "bruteforcing"
      }
    ],
    "lastupdate": 1687116861.566879
  },
  "1759": {
    "problemId": "1759",
    "problemLevel": 11,
    "problemName": "암호 만들기",
    "average_try": 2.244,
    "solvedtags": [
      {
        "bojTagId": 5,
        "key": "backtracking"
      },
      {
        "bojTagId": 125,
        "key": "bruteforcing"
      },
      {
        "bojTagId": 6,
        "key": "combinatorics"
      },
      {
        "bojTagId": 124,
        "key": "math"
      }
    ],
    "lastupdate": 1687116861.566897
  },
  "15684": {
    "problemId": "15684",
    "problemLevel": 13,
    "problemName": "사다리 조작",
    "average_try": 4.6078,
    "solvedtags": [
      {
        "bojTagId": 5,
        "key": "backtracking"
      },
      {
        "bojTagId": 125,
        "key": "bruteforcing"
      },
      {
        "bojTagId": 102,
        "key": "implementation"
      }
    ],
    "lastupdate": 1687116861.566915
  },
  "1038": {
    "problemId": "1038",
    "problemLevel": 11,
    "problemName": "감소하는 수",
    "average_try": 2.9807,
    "solvedtags": [
      {
        "bojTagId": 5,
        "key": "backtracking"
      },
      {
        "bojTagId": 125,
        "key": "bruteforcing"
      }
    ],
    "lastupdate": 1687116861.566934
  },
  "2023": {
    "problemId": "2023",
    "problemLevel": 11,
    "problemName": "신기한 소수",
    "average_try": 2.218,
    "solvedtags": [
      {
        "bojTagId": 5,
        "key": "backtracking"
      },
      {
        "bojTagId": 124,
        "key": "math"
      },
      {
        "bojTagId": 95,
        "key": "number_theory"
      },
      {
        "bojTagId": 9,
        "key": "primality_test"
      }
    ],
    "lastupdate": 1687116861.566952
  },
  "1405": {
    "problemId": "1405",
    "problemLevel": 12,
    "problemName": "미친 로봇",
    "average_try": 2.5103,
    "solvedtags": [
      {
        "bojTagId": 5,
        "key": "backtracking"
      },
      {
        "bojTagId": 125,
        "key": "bruteforcing"
      },
      {
        "bojTagId": 127,
        "key": "dfs"
      },
      {
        "bojTagId": 7,
        "key": "graphs"
      },
      {
        "bojTagId": 11,
        "key": "graph_traversal"
      },
      {
        "bojTagId": 124,
        "key": "math"
      },
      {
        "bojTagId": 177,
        "key": "probability"
      }
    ],
    "lastupdate": 1687116861.56697
  },
  "1342": {
    "problemId": "1342",
    "problemLevel": 10,
    "problemName": "행운의 문자열",
    "average_try": 2.404,
    "solvedtags": [
      {
        "bojTagId": 5,
        "key": "backtracking"
      },
      {
        "bojTagId": 125,
        "key": "bruteforcing"
      },
      {
        "bojTagId": 6,
        "key": "combinatorics"
      },
      {
        "bojTagId": 124,
        "key": "math"
      }
    ],
    "lastupdate": 1687116861.566988
  },
  "7490": {
    "problemId": "7490",
    "problemLevel": 11,
    "problemName": "0 만들기",
    "average_try": 2.0904,
    "solvedtags": [
      {
        "bojTagId": 5,
        "key": "backtracking"
      },
      {
        "bojTagId": 125,
        "key": "bruteforcing"
      },
      {
        "bojTagId": 102,
        "key": "implementation"
      },
      {
        "bojTagId": 158,
        "key": "string"
      }
    ],
    "lastupdate": 1687116861.567005
  },
  "13908": {
    "problemId": "13908",
    "problemLevel": 9,
    "problemName": "비밀번호",
    "average_try": 2.3068,
    "solvedtags": [
      {
        "bojTagId": 125,
        "key": "bruteforcing"
      }
    ],
    "lastupdate": 1687116861.567022
  },
  "7682": {
    "problemId": "7682",
    "problemLevel": 11,
    "problemName": "틱택토",
    "average_try": 3.4482,
    "solvedtags": [
      {
        "bojTagId": 102,
        "key": "implementation"
      }
    ],
    "lastupdate": 1687116861.567039
  },
  "20208": {
    "problemId": "20208",
    "problemLevel": 11,
    "problemName": "진우의 민트초코우유",
    "average_try": 2.4158,
    "solvedtags": [
      {
        "bojTagId": 5,
        "key": "backtracking"
      },
      {
        "bojTagId": 125,
        "key": "bruteforcing"
      }
    ],
    "lastupdate": 1687116861.567056
  },
  "1469": {
    "problemId": "1469",
    "problemLevel": 11,
    "problemName": "숌 사이 수열",
    "average_try": 3.0857,
    "solvedtags": [
      {
        "bojTagId": 5,
        "key": "backtracking"
      },
      {
        "bojTagId": 125,
        "key": "bruteforcing"
      }
    ],
    "lastupdate": 1687116861.567074
  },
  "10421": {
    "problemId": "10421",
    "problemLevel": 11,
    "problemName": "수식 완성하기",
    "average_try": 3.9844,
    "solvedtags": [
      {
        "bojTagId": 5,
        "key": "backtracking"
      },
      {
        "bojTagId": 125,
        "key": "bruteforcing"
      }
    ],
    "lastupdate": 1687116861.567091
  },
  "1987": {
    "problemId": "1987",
    "problemLevel": 12,
    "problemName": "알파벳",
    "average_try": 3.4259,
    "solvedtags": [
      {
        "bojTagId": 5,
        "key": "backtracking"
      },
      {
        "bojTagId": 127,
        "key": "dfs"
      },
      {
        "bojTagId": 7,
        "key": "graphs"
      },
      {
        "bojTagId": 11,
        "key": "graph_traversal"
      }
    ],
    "lastupdate": 1687116861.567109
  },
  "2580": {
    "problemId": "2580",
    "problemLevel": 12,
    "problemName": "스도쿠",
    "average_try": 3.7263,
    "solvedtags": [
      {
        "bojTagId": 5,
        "key": "backtracking"
      }
    ],
    "lastupdate": 1687116861.567126
  },
  "1062": {
    "problemId": "1062",
    "problemLevel": 12,
    "problemName": "가르침",
    "average_try": 3.9631,
    "solvedtags": [
      {
        "bojTagId": 5,
        "key": "backtracking"
      },
      {
        "bojTagId": 14,
        "key": "bitmask"
      },
      {
        "bojTagId": 125,
        "key": "bruteforcing"
      }
    ],
    "lastupdate": 1687116861.567144
  },
  "2661": {
    "problemId": "2661",
    "problemLevel": 12,
    "problemName": "좋은수열",
    "average_try": 2.0063,
    "solvedtags": [
      {
        "bojTagId": 5,
        "key": "backtracking"
      }
    ],
    "lastupdate": 1687116861.567161
  },
  "2239": {
    "problemId": "2239",
    "problemLevel": 12,
    "problemName": "스도쿠",
    "average_try": 2.1705,
    "solvedtags": [
      {
        "bojTagId": 5,
        "key": "backtracking"
      },
      {
        "bojTagId": 102,
        "key": "implementation"
      }
    ],
    "lastupdate": 1687116861.567179
  },
  "3980": {
    "problemId": "3980",
    "problemLevel": 11,
    "problemName": "선발 명단",
    "average_try": 2.2941,
    "solvedtags": [
      {
        "bojTagId": 5,
        "key": "backtracking"
      },
      {
        "bojTagId": 125,
        "key": "bruteforcing"
      }
    ],
    "lastupdate": 1687116861.567196
  },
  "16938": {
    "problemId": "16938",
    "problemLevel": 11,
    "problemName": "캠프 준비",
    "average_try": 1.423,
    "solvedtags": [
      {
        "bojTagId": 5,
        "key": "backtracking"
      },
      {
        "bojTagId": 14,
        "key": "bitmask"
      },
      {
        "bojTagId": 125,
        "key": "bruteforcing"
      }
    ],
    "lastupdate": 1687116861.567214
  },
  "2922": {
    "problemId": "2922",
    "problemLevel": 11,
    "problemName": "즐거운 단어",
    "average_try": 2.1331,
    "solvedtags": [
      {
        "bojTagId": 5,
        "key": "backtracking"
      },
      {
        "bojTagId": 125,
        "key": "bruteforcing"
      }
    ],
    "lastupdate": 1687116861.567232
  },
  "15918": {
    "problemId": "15918",
    "problemLevel": 11,
    "problemName": "랭퍼든 수열쟁이야!!",
    "average_try": 1.2976,
    "solvedtags": [
      {
        "bojTagId": 5,
        "key": "backtracking"
      }
    ],
    "lastupdate": 1687116861.56725
  },
  "1941": {
    "problemId": "1941",
    "problemLevel": 13,
    "problemName": "소문난 칠공주",
    "average_try": 1.9733,
    "solvedtags": [
      {
        "bojTagId": 5,
        "key": "backtracking"
      },
      {
        "bojTagId": 126,
        "key": "bfs"
      },
      {
        "bojTagId": 125,
        "key": "bruteforcing"
      },
      {
        "bojTagId": 6,
        "key": "combinatorics"
      },
      {
        "bojTagId": 127,
        "key": "dfs"
      },
      {
        "bojTagId": 7,
        "key": "graphs"
      },
      {
        "bojTagId": 11,
        "key": "graph_traversal"
      },
      {
        "bojTagId": 124,
        "key": "math"
      }
    ],
    "lastupdate": 1687116861.567268
  },
  "1248": {
    "problemId": "1248",
    "problemLevel": 13,
    "problemName": "Guess",
    "average_try": 2.792,
    "solvedtags": [
      {
        "bojTagId": 5,
        "key": "backtracking"
      },
      {
        "bojTagId": 125,
        "key": "bruteforcing"
      }
    ],
    "lastupdate": 1687116861.567286
  },
  "9944": {
    "problemId": "9944",
    "problemLevel": 13,
    "problemName": "NxM 보드 완주하기",
    "average_try": 3.3107,
    "solvedtags": [
      {
        "bojTagId": 5,
        "key": "backtracking"
      },
      {
        "bojTagId": 102,
        "key": "implementation"
      }
    ],
    "lastupdate": 1687116861.567304
  },
  "6443": {
    "problemId": "6443",
    "problemLevel": 11,
    "problemName": "애너그램",
    "average_try": 3.0999,
    "solvedtags": [
      {
        "bojTagId": 5,
        "key": "backtracking"
      },
      {
        "bojTagId": 158,
        "key": "string"
      }
    ],
    "lastupdate": 1687116861.567322
  },
  "2026": {
    "problemId": "2026",
    "problemLevel": 13,
    "problemName": "소풍",
    "average_try": 4.3127,
    "solvedtags": [
      {
        "bojTagId": 5,
        "key": "backtracking"
      }
    ],
    "lastupdate": 1687116861.56734
  },
  "15659": {
    "problemId": "15659",
    "problemLevel": 12,
    "problemName": "연산자 끼워넣기 (3)",
    "average_try": 1.7232,
    "solvedtags": [
      {
        "bojTagId": 5,
        "key": "backtracking"
      },
      {
        "bojTagId": 125,
        "key": "bruteforcing"
      },
      {
        "bojTagId": 175,
        "key": "data_structures"
      },
      {
        "bojTagId": 71,
        "key": "stack"
      }
    ],
    "lastupdate": 1687116861.567358
  },
  "12908": {
    "problemId": "12908",
    "problemLevel": 11,
    "problemName": "텔레포트 3",
    "average_try": 2.2109,
    "solvedtags": [
      {
        "bojTagId": 5,
        "key": "backtracking"
      },
      {
        "bojTagId": 125,
        "key": "bruteforcing"
      },
      {
        "bojTagId": 31,
        "key": "floyd_warshall"
      },
      {
        "bojTagId": 7,
        "key": "graphs"
      }
    ],
    "lastupdate": 1687116861.567376
  },
  "1729": {
    "problemId": "1729",
    "problemLevel": 15,
    "problemName": "이차원 배열의 합",
    "average_try": 3.2857,
    "solvedtags": [
      {
        "bojTagId": 5,
        "key": "backtracking"
      },
      {
        "bojTagId": 125,
        "key": "bruteforcing"
      }
    ],
    "lastupdate": 1687116861.567393
  },
  "17136": {
    "problemId": "17136",
    "problemLevel": 14,
    "problemName": "색종이 붙이기",
    "average_try": 2.8672,
    "solvedtags": [
      {
        "bojTagId": 5,
        "key": "backtracking"
      },
      {
        "bojTagId": 125,
        "key": "bruteforcing"
      }
    ],
    "lastupdate": 1687116861.567411
  },
  "1799": {
    "problemId": "1799",
    "problemLevel": 15,
    "problemName": "비숍",
    "average_try": 4.1331,
    "solvedtags": [
      {
        "bojTagId": 5,
        "key": "backtracking"
      }
    ],
    "lastupdate": 1687116861.567428
  },
  "16571": {
    "problemId": "16571",
    "problemLevel": 13,
    "problemName": "알파 틱택토",
    "average_try": 2.4684,
    "solvedtags": [
      {
        "bojTagId": 5,
        "key": "backtracking"
      },
      {
        "bojTagId": 140,
        "key": "game_theory"
      }
    ],
    "lastupdate": 1687116861.567445
  },
  "3165": {
    "problemId": "3165",
    "problemLevel": 13,
    "problemName": "5",
    "average_try": 3.939,
    "solvedtags": [
      {
        "bojTagId": 5,
        "key": "backtracking"
      },
      {
        "bojTagId": 33,
        "key": "greedy"
      }
    ],
    "lastupdate": 1687116861.567462
  },
  "1789": {
    "problemId": "1789",
    "problemLevel": 6,
    "problemName": "수들의 합",
    "average_try": 2.3922,
    "solvedtags": [
      {
        "bojTagId": 33,
        "key": "greedy"
      },
      {
        "bojTagId": 124,
        "key": "math"
      }
    ],
    "lastupdate": 1687116861.568379
  },
  "2417": {
    "problemId": "2417",
    "problemLevel": 7,
    "problemName": "정수 제곱근",
    "average_try": 3.676,
    "solvedtags": [
      {
        "bojTagId": 12,
        "key": "binary_search"
      },
      {
        "bojTagId": 124,
        "key": "math"
      }
    ],
    "lastupdate": 1687116861.568407
  },
  "17266": {
    "problemId": "17266",
    "problemLevel": 7,
    "problemName": "어두운 굴다리",
    "average_try": 2.4803,
    "solvedtags": [
      {
        "bojTagId": 12,
        "key": "binary_search"
      },
      {
        "bojTagId": 102,
        "key": "implementation"
      },
      {
        "bojTagId": 106,
        "key": "sweeping"
      }
    ],
    "lastupdate": 1687116861.568428
  },
  "1920": {
    "problemId": "1920",
    "problemLevel": 7,
    "problemName": "수 찾기",
    "average_try": 3.3366,
    "solvedtags": [
      {
        "bojTagId": 12,
        "key": "binary_search"
      },
      {
        "bojTagId": 175,
        "key": "data_structures"
      },
      {
        "bojTagId": 97,
        "key": "sorting"
      }
    ],
    "lastupdate": 1687116861.568447
  },
  "10815": {
    "problemId": "10815",
    "problemLevel": 6,
    "problemName": "숫자 카드",
    "average_try": 2.2655,
    "solvedtags": [
      {
        "bojTagId": 12,
        "key": "binary_search"
      },
      {
        "bojTagId": 175,
        "key": "data_structures"
      },
      {
        "bojTagId": 136,
        "key": "hash_set"
      },
      {
        "bojTagId": 97,
        "key": "sorting"
      }
    ],
    "lastupdate": 1687116861.568465
  },
  "10816": {
    "problemId": "10816",
    "problemLevel": 7,
    "problemName": "숫자 카드 2",
    "average_try": 2.7231,
    "solvedtags": [
      {
        "bojTagId": 12,
        "key": "binary_search"
      },
      {
        "bojTagId": 175,
        "key": "data_structures"
      },
      {
        "bojTagId": 136,
        "key": "hash_set"
      },
      {
        "bojTagId": 97,
        "key": "sorting"
      }
    ],
    "lastupdate": 1687116861.568483
  },
  "20551": {
    "problemId": "20551",
    "problemLevel": 7,
    "problemName": "Sort 마스터 배지훈의 후계자",
    "average_try": 2.8035,
    "solvedtags": [
      {
        "bojTagId": 12,
        "key": "binary_search"
      },
      {
        "bojTagId": 175,
        "key": "data_structures"
      },
      {
        "bojTagId": 97,
        "key": "sorting"
      }
    ],
    "lastupdate": 1687116861.568501
  },
  "2805": {
    "problemId": "2805",
    "problemLevel": 9,
    "problemName": "나무 자르기",
    "average_try": 3.883,
    "solvedtags": [
      {
        "bojTagId": 12,
        "key": "binary_search"
      },
      {
        "bojTagId": 170,
        "key": "parametric_search"
      }
    ],
    "lastupdate": 1687116861.568518
  },
  "1654": {
    "problemId": "1654",
    "problemLevel": 9,
    "problemName": "랜선 자르기",
    "average_try": 4.7246,
    "solvedtags": [
      {
        "bojTagId": 12,
        "key": "binary_search"
      },
      {
        "bojTagId": 170,
        "key": "parametric_search"
      }
    ],
    "lastupdate": 1687116861.568537
  },
  "2512": {
    "problemId": "2512",
    "problemLevel": 8,
    "problemName": "예산",
    "average_try": 2.8635,
    "solvedtags": [
      {
        "bojTagId": 12,
        "key": "binary_search"
      },
      {
        "bojTagId": 170,
        "key": "parametric_search"
      }
    ],
    "lastupdate": 1687116861.568555
  },
  "1072": {
    "problemId": "1072",
    "problemLevel": 8,
    "problemName": "게임",
    "average_try": 4.2138,
    "solvedtags": [
      {
        "bojTagId": 12,
        "key": "binary_search"
      },
      {
        "bojTagId": 124,
        "key": "math"
      }
    ],
    "lastupdate": 1687116861.568573
  },
  "6236": {
    "problemId": "6236",
    "problemLevel": 9,
    "problemName": "용돈 관리",
    "average_try": 3.4604,
    "solvedtags": [
      {
        "bojTagId": 12,
        "key": "binary_search"
      },
      {
        "bojTagId": 170,
        "key": "parametric_search"
      }
    ],
    "lastupdate": 1687116861.568609
  },
  "7795": {
    "problemId": "7795",
    "problemLevel": 8,
    "problemName": "먹을 것인가 먹힐 것인가",
    "average_try": 2.0026,
    "solvedtags": [
      {
        "bojTagId": 12,
        "key": "binary_search"
      },
      {
        "bojTagId": 97,
        "key": "sorting"
      },
      {
        "bojTagId": 80,
        "key": "two_pointer"
      }
    ],
    "lastupdate": 1687116861.568626
  },
  "2792": {
    "problemId": "2792",
    "problemLevel": 10,
    "problemName": "보석 상자",
    "average_try": 2.6406,
    "solvedtags": [
      {
        "bojTagId": 12,
        "key": "binary_search"
      },
      {
        "bojTagId": 170,
        "key": "parametric_search"
      }
    ],
    "lastupdate": 1687116861.568644
  },
  "16401": {
    "problemId": "16401",
    "problemLevel": 9,
    "problemName": "과자 나눠주기",
    "average_try": 2.7128,
    "solvedtags": [
      {
        "bojTagId": 12,
        "key": "binary_search"
      },
      {
        "bojTagId": 170,
        "key": "parametric_search"
      }
    ],
    "lastupdate": 1687116861.568662
  },
  "13702": {
    "problemId": "13702",
    "problemLevel": 8,
    "problemName": "이상한 술집",
    "average_try": 3.3128,
    "solvedtags": [
      {
        "bojTagId": 12,
        "key": "binary_search"
      }
    ],
    "lastupdate": 1687116861.56868
  },
  "11561": {
    "problemId": "11561",
    "problemLevel": 8,
    "problemName": "징검다리",
    "average_try": 3.1908,
    "solvedtags": [
      {
        "bojTagId": 12,
        "key": "binary_search"
      },
      {
        "bojTagId": 124,
        "key": "math"
      }
    ],
    "lastupdate": 1687116861.568698
  },
  "14627": {
    "problemId": "14627",
    "problemLevel": 9,
    "problemName": "파닭파닭",
    "average_try": 5.0085,
    "solvedtags": [
      {
        "bojTagId": 12,
        "key": "binary_search"
      }
    ],
    "lastupdate": 1687116861.568716
  },
  "1166": {
    "problemId": "1166",
    "problemLevel": 8,
    "problemName": "선물",
    "average_try": 4.8614,
    "solvedtags": [
      {
        "bojTagId": 12,
        "key": "binary_search"
      }
    ],
    "lastupdate": 1687116861.568747
  },
  "17451": {
    "problemId": "17451",
    "problemLevel": 8,
    "problemName": "평행 우주",
    "average_try": 2.8761,
    "solvedtags": [
      {
        "bojTagId": 33,
        "key": "greedy"
      },
      {
        "bojTagId": 124,
        "key": "math"
      }
    ],
    "lastupdate": 1687116861.568765
  },
  "19637": {
    "problemId": "19637",
    "problemLevel": 8,
    "problemName": "IF문 좀 대신 써줘",
    "average_try": 2.8405,
    "solvedtags": [
      {
        "bojTagId": 12,
        "key": "binary_search"
      }
    ],
    "lastupdate": 1687116861.568783
  },
  "17393": {
    "problemId": "17393",
    "problemLevel": 7,
    "problemName": "다이나믹 롤러",
    "average_try": 2.4093,
    "solvedtags": [
      {
        "bojTagId": 12,
        "key": "binary_search"
      }
    ],
    "lastupdate": 1687116861.568802
  },
  "17124": {
    "problemId": "17124",
    "problemLevel": 8,
    "problemName": "두 개의 배열",
    "average_try": 2.809,
    "solvedtags": [
      {
        "bojTagId": 12,
        "key": "binary_search"
      },
      {
        "bojTagId": 97,
        "key": "sorting"
      }
    ],
    "lastupdate": 1687116861.56882
  },
  "11663": {
    "problemId": "11663",
    "problemLevel": 8,
    "problemName": "선분 위의 점",
    "average_try": 2.801,
    "solvedtags": [
      {
        "bojTagId": 12,
        "key": "binary_search"
      },
      {
        "bojTagId": 97,
        "key": "sorting"
      }
    ],
    "lastupdate": 1687116861.568837
  },
  "15810": {
    "problemId": "15810",
    "problemLevel": 9,
    "problemName": "풍선 공장",
    "average_try": 3.6017,
    "solvedtags": [
      {
        "bojTagId": 12,
        "key": "binary_search"
      },
      {
        "bojTagId": 170,
        "key": "parametric_search"
      }
    ],
    "lastupdate": 1687116861.568855
  },
  "17503": {
    "problemId": "17503",
    "problemLevel": 10,
    "problemName": "맥주 축제",
    "average_try": 3.4815,
    "solvedtags": [
      {
        "bojTagId": 12,
        "key": "binary_search"
      },
      {
        "bojTagId": 175,
        "key": "data_structures"
      },
      {
        "bojTagId": 33,
        "key": "greedy"
      },
      {
        "bojTagId": 59,
        "key": "priority_queue"
      },
      {
        "bojTagId": 97,
        "key": "sorting"
      }
    ],
    "lastupdate": 1687116861.568873
  },
  "18113": {
    "problemId": "18113",
    "problemLevel": 9,
    "problemName": "그르다 김가놈",
    "average_try": 3.479,
    "solvedtags": [
      {
        "bojTagId": 12,
        "key": "binary_search"
      }
    ],
    "lastupdate": 1687116861.568891
  },
  "2121": {
    "problemId": "2121",
    "problemLevel": 8,
    "problemName": "넷이 놀기",
    "average_try": 2.5934,
    "solvedtags": [
      {
        "bojTagId": 12,
        "key": "binary_search"
      },
      {
        "bojTagId": 175,
        "key": "data_structures"
      },
      {
        "bojTagId": 100,
        "key": "geometry"
      },
      {
        "bojTagId": 136,
        "key": "hash_set"
      }
    ],
    "lastupdate": 1687116861.568909
  },
  "2110": {
    "problemId": "2110",
    "problemLevel": 12,
    "problemName": "공유기 설치",
    "average_try": 2.7836,
    "solvedtags": [
      {
        "bojTagId": 12,
        "key": "binary_search"
      },
      {
        "bojTagId": 170,
        "key": "parametric_search"
      }
    ],
    "lastupdate": 1687116861.568927
  },
  "2343": {
    "problemId": "2343",
    "problemLevel": 10,
    "problemName": "기타 레슨",
    "average_try": 3.2055,
    "solvedtags": [
      {
        "bojTagId": 12,
        "key": "binary_search"
      },
      {
        "bojTagId": 170,
        "key": "parametric_search"
      }
    ],
    "lastupdate": 1687116861.568946
  },
  "3079": {
    "problemId": "3079",
    "problemLevel": 11,
    "problemName": "입국심사",
    "average_try": 3.9433,
    "solvedtags": [
      {
        "bojTagId": 12,
        "key": "binary_search"
      },
      {
        "bojTagId": 170,
        "key": "parametric_search"
      }
    ],
    "lastupdate": 1687116861.568965
  },
  "2022": {
    "problemId": "2022",
    "problemLevel": 12,
    "problemName": "사다리",
    "average_try": 1.8148,
    "solvedtags": [
      {
        "bojTagId": 12,
        "key": "binary_search"
      },
      {
        "bojTagId": 100,
        "key": "geometry"
      },
      {
        "bojTagId": 124,
        "key": "math"
      },
      {
        "bojTagId": 60,
        "key": "pythagoras"
      }
    ],
    "lastupdate": 1687116861.568983
  },
  "16564": {
    "problemId": "16564",
    "problemLevel": 10,
    "problemName": "히오스 프로게이머",
    "average_try": 2.7549,
    "solvedtags": [
      {
        "bojTagId": 12,
        "key": "binary_search"
      },
      {
        "bojTagId": 170,
        "key": "parametric_search"
      }
    ],
    "lastupdate": 1687116861.569001
  },
  "11687": {
    "problemId": "11687",
    "problemLevel": 10,
    "problemName": "팩토리얼 0의 개수",
    "average_try": 2.3033,
    "solvedtags": [
      {
        "bojTagId": 12,
        "key": "binary_search"
      },
      {
        "bojTagId": 124,
        "key": "math"
      },
      {
        "bojTagId": 95,
        "key": "number_theory"
      }
    ],
    "lastupdate": 1687116861.569018
  },
  "18114": {
    "problemId": "18114",
    "problemLevel": 11,
    "problemName": "블랙 프라이데이",
    "average_try": 4.3371,
    "solvedtags": [
      {
        "bojTagId": 12,
        "key": "binary_search"
      },
      {
        "bojTagId": 125,
        "key": "bruteforcing"
      },
      {
        "bojTagId": 97,
        "key": "sorting"
      }
    ],
    "lastupdate": 1687116861.569035
  },
  "14575": {
    "problemId": "14575",
    "problemLevel": 10,
    "problemName": "뒤풀이",
    "average_try": 3.4426,
    "solvedtags": [
      {
        "bojTagId": 12,
        "key": "binary_search"
      },
      {
        "bojTagId": 170,
        "key": "parametric_search"
      }
    ],
    "lastupdate": 1687116861.569053
  },
  "17179": {
    "problemId": "17179",
    "problemLevel": 11,
    "problemName": "케이크 자르기",
    "average_try": 3.0909,
    "solvedtags": [
      {
        "bojTagId": 12,
        "key": "binary_search"
      },
      {
        "bojTagId": 170,
        "key": "parametric_search"
      }
    ],
    "lastupdate": 1687116861.569071
  },
  "16960": {
    "problemId": "16960",
    "problemLevel": 7,
    "problemName": "스위치와 램프",
    "average_try": 1.8187,
    "solvedtags": [
      {
        "bojTagId": 102,
        "key": "implementation"
      }
    ],
    "lastupdate": 1687116861.569089
  },
  "20495": {
    "problemId": "20495",
    "problemLevel": 10,
    "problemName": "수열과 헌팅",
    "average_try": 2.2266,
    "solvedtags": [
      {
        "bojTagId": 12,
        "key": "binary_search"
      }
    ],
    "lastupdate": 1687116861.569106
  },
  "3020": {
    "problemId": "3020",
    "problemLevel": 11,
    "problemName": "개똥벌레",
    "average_try": 2.272,
    "solvedtags": [
      {
        "bojTagId": 12,
        "key": "binary_search"
      },
      {
        "bojTagId": 139,
        "key": "prefix_sum"
      }
    ],
    "lastupdate": 1687116861.569142
  },
  "1477": {
    "problemId": "1477",
    "problemLevel": 12,
    "problemName": "휴게소 세우기",
    "average_try": 3.3185,
    "solvedtags": [
      {
        "bojTagId": 12,
        "key": "binary_search"
      },
      {
        "bojTagId": 170,
        "key": "parametric_search"
      }
    ],
    "lastupdate": 1687116861.569178
  },
  "2866": {
    "problemId": "2866",
    "problemLevel": 11,
    "problemName": "문자열 잘라내기",
    "average_try": 2.737,
    "solvedtags": [
      {
        "bojTagId": 12,
        "key": "binary_search"
      },
      {
        "bojTagId": 175,
        "key": "data_structures"
      },
      {
        "bojTagId": 136,
        "key": "hash_set"
      },
      {
        "bojTagId": 97,
        "key": "sorting"
      },
      {
        "bojTagId": 158,
        "key": "string"
      }
    ],
    "lastupdate": 1687116861.569196
  },
  "20444": {
    "problemId": "20444",
    "problemLevel": 11,
    "problemName": "색종이와 가위",
    "average_try": 2.9609,
    "solvedtags": [
      {
        "bojTagId": 12,
        "key": "binary_search"
      },
      {
        "bojTagId": 124,
        "key": "math"
      }
    ],
    "lastupdate": 1687116861.569213
  },
  "1939": {
    "problemId": "1939",
    "problemLevel": 13,
    "problemName": "중량제한",
    "average_try": 3.9303,
    "solvedtags": [
      {
        "bojTagId": 126,
        "key": "bfs"
      },
      {
        "bojTagId": 12,
        "key": "binary_search"
      },
      {
        "bojTagId": 175,
        "key": "data_structures"
      },
      {
        "bojTagId": 81,
        "key": "disjoint_set"
      },
      {
        "bojTagId": 7,
        "key": "graphs"
      },
      {
        "bojTagId": 11,
        "key": "graph_traversal"
      }
    ],
    "lastupdate": 1687116861.569249
  },
  "8983": {
    "problemId": "8983",
    "problemLevel": 12,
    "problemName": "사냥꾼",
    "average_try": 3.0987,
    "solvedtags": [
      {
        "bojTagId": 12,
        "key": "binary_search"
      },
      {
        "bojTagId": 97,
        "key": "sorting"
      }
    ],
    "lastupdate": 1687116861.569267
  },
  "13397": {
    "problemId": "13397",
    "problemLevel": 12,
    "problemName": "구간 나누기 2",
    "average_try": 1.5129,
    "solvedtags": [
      {
        "bojTagId": 12,
        "key": "binary_search"
      },
      {
        "bojTagId": 170,
        "key": "parametric_search"
      }
    ],
    "lastupdate": 1687116861.569302
  },
  "9007": {
    "problemId": "9007",
    "problemLevel": 14,
    "problemName": "카누 선수",
    "average_try": 3.8789,
    "solvedtags": [
      {
        "bojTagId": 12,
        "key": "binary_search"
      },
      {
        "bojTagId": 46,
        "key": "mitm"
      },
      {
        "bojTagId": 97,
        "key": "sorting"
      }
    ],
    "lastupdate": 1687116861.569319
  },
  "2412": {
    "problemId": "2412",
    "problemLevel": 12,
    "problemName": "암벽 등반",
    "average_try": 3.1981,
    "solvedtags": [
      {
        "bojTagId": 126,
        "key": "bfs"
      },
      {
        "bojTagId": 12,
        "key": "binary_search"
      },
      {
        "bojTagId": 175,
        "key": "data_structures"
      },
      {
        "bojTagId": 7,
        "key": "graphs"
      },
      {
        "bojTagId": 11,
        "key": "graph_traversal"
      },
      {
        "bojTagId": 136,
        "key": "hash_set"
      }
    ],
    "lastupdate": 1687116861.569337
  },
  "17951": {
    "problemId": "17951",
    "problemLevel": 12,
    "problemName": "흩날리는 시험지 속에서 내 평점이 느껴진거야",
    "average_try": 2,
    "solvedtags": [
      {
        "bojTagId": 12,
        "key": "binary_search"
      },
      {
        "bojTagId": 170,
        "key": "parametric_search"
      }
    ],
    "lastupdate": 1687116861.569355
  },
  "12757": {
    "problemId": "12757",
    "problemLevel": 13,
    "problemName": "전설의 JBNU",
    "average_try": 3.3821,
    "solvedtags": [
      {
        "bojTagId": 12,
        "key": "binary_search"
      },
      {
        "bojTagId": 175,
        "key": "data_structures"
      },
      {
        "bojTagId": 136,
        "key": "hash_set"
      }
    ],
    "lastupdate": 1687116861.569373
  },
  "1300": {
    "problemId": "1300",
    "problemLevel": 14,
    "problemName": "K번째 수",
    "average_try": 2.6747,
    "solvedtags": [
      {
        "bojTagId": 12,
        "key": "binary_search"
      },
      {
        "bojTagId": 170,
        "key": "parametric_search"
      }
    ],
    "lastupdate": 1687116861.569391
  },
  "2143": {
    "problemId": "2143",
    "problemLevel": 13,
    "problemName": "두 배열의 합",
    "average_try": 3.2344,
    "solvedtags": [
      {
        "bojTagId": 12,
        "key": "binary_search"
      },
      {
        "bojTagId": 175,
        "key": "data_structures"
      },
      {
        "bojTagId": 139,
        "key": "prefix_sum"
      }
    ],
    "lastupdate": 1687116861.569408
  },
  "16434": {
    "problemId": "16434",
    "problemLevel": 12,
    "problemName": "드래곤 앤 던전",
    "average_try": 3.7145,
    "solvedtags": [
      {
        "bojTagId": 12,
        "key": "binary_search"
      },
      {
        "bojTagId": 102,
        "key": "implementation"
      }
    ],
    "lastupdate": 1687116861.569425
  },
  "15823": {
    "problemId": "15823",
    "problemLevel": 14,
    "problemName": "카드 팩 구매하기",
    "average_try": 3.6832,
    "solvedtags": [
      {
        "bojTagId": 12,
        "key": "binary_search"
      },
      {
        "bojTagId": 80,
        "key": "two_pointer"
      }
    ],
    "lastupdate": 1687116861.569443
  },
  "2613": {
    "problemId": "2613",
    "problemLevel": 14,
    "problemName": "숫자구슬",
    "average_try": 3.7191,
    "solvedtags": [
      {
        "bojTagId": 12,
        "key": "binary_search"
      },
      {
        "bojTagId": 25,
        "key": "dp"
      },
      {
        "bojTagId": 33,
        "key": "greedy"
      },
      {
        "bojTagId": 170,
        "key": "parametric_search"
      }
    ],
    "lastupdate": 1687116861.569477
  },
  "1561": {
    "problemId": "1561",
    "problemLevel": 14,
    "problemName": "놀이 공원",
    "average_try": 3.9448,
    "solvedtags": [
      {
        "bojTagId": 12,
        "key": "binary_search"
      },
      {
        "bojTagId": 170,
        "key": "parametric_search"
      }
    ],
    "lastupdate": 1687116861.569495
  },
  "15732": {
    "problemId": "15732",
    "problemLevel": 14,
    "problemName": "도토리 숨기기",
    "average_try": 3.6343,
    "solvedtags": [
      {
        "bojTagId": 12,
        "key": "binary_search"
      }
    ],
    "lastupdate": 1687116861.569512
  },
  "6209": {
    "problemId": "6209",
    "problemLevel": 13,
    "problemName": "제자리 멀리뛰기",
    "average_try": 2.4805,
    "solvedtags": [
      {
        "bojTagId": 12,
        "key": "binary_search"
      },
      {
        "bojTagId": 33,
        "key": "greedy"
      },
      {
        "bojTagId": 170,
        "key": "parametric_search"
      }
    ],
    "lastupdate": 1687116861.56953
  },
  "9094": {
    "problemId": "9094",
    "problemLevel": 3,
    "problemName": "수학적 호기심",
    "average_try": 1.7269,
    "solvedtags": [
      {
        "bojTagId": 125,
        "key": "bruteforcing"
      },
      {
        "bojTagId": 124,
        "key": "math"
      }
    ],
    "lastupdate": 1687116861.570489
  },
  "4690": {
    "problemId": "4690",
    "problemLevel": 3,
    "problemName": "완전 세제곱",
    "average_try": 2.5588,
    "solvedtags": [
      {
        "bojTagId": 125,
        "key": "bruteforcing"
      },
      {
        "bojTagId": 102,
        "key": "implementation"
      },
      {
        "bojTagId": 124,
        "key": "math"
      }
    ],
    "lastupdate": 1687116861.570536
  },
  "3040": {
    "problemId": "3040",
    "problemLevel": 4,
    "problemName": "백설 공주와 일곱 난쟁이",
    "average_try": 1.4469,
    "solvedtags": [
      {
        "bojTagId": 125,
        "key": "bruteforcing"
      }
    ],
    "lastupdate": 1687116861.570557
  },
  "10448": {
    "problemId": "10448",
    "problemLevel": 5,
    "problemName": "유레카 이론",
    "average_try": 1.7369,
    "solvedtags": [
      {
        "bojTagId": 125,
        "key": "bruteforcing"
      },
      {
        "bojTagId": 124,
        "key": "math"
      }
    ],
    "lastupdate": 1687116861.570577
  },
  "2798": {
    "problemId": "2798",
    "problemLevel": 4,
    "problemName": "블랙잭",
    "average_try": 2.0856,
    "solvedtags": [
      {
        "bojTagId": 125,
        "key": "bruteforcing"
      }
    ],
    "lastupdate": 1687116861.570596
  },
  "2309": {
    "problemId": "2309",
    "problemLevel": 5,
    "problemName": "일곱 난쟁이",
    "average_try": 2.3878,
    "solvedtags": [
      {
        "bojTagId": 125,
        "key": "bruteforcing"
      },
      {
        "bojTagId": 97,
        "key": "sorting"
      }
    ],
    "lastupdate": 1687116861.570615
  },
  "2231": {
    "problemId": "2231",
    "problemLevel": 4,
    "problemName": "분해합",
    "average_try": 2.2054,
    "solvedtags": [
      {
        "bojTagId": 125,
        "key": "bruteforcing"
      }
    ],
    "lastupdate": 1687116861.570633
  },
  "14697": {
    "problemId": "14697",
    "problemLevel": 4,
    "problemName": "방 배정하기",
    "average_try": 2.3378,
    "solvedtags": [
      {
        "bojTagId": 125,
        "key": "bruteforcing"
      }
    ],
    "lastupdate": 1687116861.570651
  },
  "1668": {
    "problemId": "1668",
    "problemLevel": 4,
    "problemName": "트로피 진열",
    "average_try": 1.9672,
    "solvedtags": [
      {
        "bojTagId": 102,
        "key": "implementation"
      }
    ],
    "lastupdate": 1687116861.570669
  },
  "13410": {
    "problemId": "13410",
    "problemLevel": 4,
    "problemName": "거꾸로 구구단",
    "average_try": 1.6375,
    "solvedtags": [
      {
        "bojTagId": 125,
        "key": "bruteforcing"
      },
      {
        "bojTagId": 124,
        "key": "math"
      }
    ],
    "lastupdate": 1687116861.570688
  },
  "19532": {
    "problemId": "19532",
    "problemLevel": 4,
    "problemName": "수학은 비대면강의입니다",
    "average_try": 1.8999,
    "solvedtags": [
      {
        "bojTagId": 125,
        "key": "bruteforcing"
      },
      {
        "bojTagId": 124,
        "key": "math"
      }
    ],
    "lastupdate": 1687116861.570707
  },
  "18312": {
    "problemId": "18312",
    "problemLevel": 4,
    "problemName": "시각",
    "average_try": 2.4854,
    "solvedtags": [
      {
        "bojTagId": 125,
        "key": "bruteforcing"
      },
      {
        "bojTagId": 102,
        "key": "implementation"
      },
      {
        "bojTagId": 158,
        "key": "string"
      }
    ],
    "lastupdate": 1687116861.570726
  },
  "1145": {
    "problemId": "1145",
    "problemLevel": 5,
    "problemName": "적어도 대부분의 배수",
    "average_try": 1.6177,
    "solvedtags": [
      {
        "bojTagId": 125,
        "key": "bruteforcing"
      }
    ],
    "lastupdate": 1687116861.570745
  },
  "2160": {
    "problemId": "2160",
    "problemLevel": 5,
    "problemName": "그림 비교",
    "average_try": 2.0333,
    "solvedtags": [
      {
        "bojTagId": 125,
        "key": "bruteforcing"
      },
      {
        "bojTagId": 102,
        "key": "implementation"
      }
    ],
    "lastupdate": 1687116861.570762
  },
  "18512": {
    "problemId": "18512",
    "problemLevel": 5,
    "problemName": "점프 점프",
    "average_try": 2.1919,
    "solvedtags": [
      {
        "bojTagId": 125,
        "key": "bruteforcing"
      },
      {
        "bojTagId": 124,
        "key": "math"
      },
      {
        "bojTagId": 95,
        "key": "number_theory"
      }
    ],
    "lastupdate": 1687116861.57078
  },
  "18868": {
    "problemId": "18868",
    "problemLevel": 5,
    "problemName": "멀티버스 Ⅰ",
    "average_try": 1.7194,
    "solvedtags": [
      {
        "bojTagId": 125,
        "key": "bruteforcing"
      }
    ],
    "lastupdate": 1687116861.570798
  },
  "15721": {
    "problemId": "15721",
    "problemLevel": 6,
    "problemName": "번데기",
    "average_try": 2.1661,
    "solvedtags": [
      {
        "bojTagId": 125,
        "key": "bruteforcing"
      },
      {
        "bojTagId": 102,
        "key": "implementation"
      },
      {
        "bojTagId": 141,
        "key": "simulation"
      }
    ],
    "lastupdate": 1687116861.570816
  },
  "1969": {
    "problemId": "1969",
    "problemLevel": 7,
    "problemName": "DNA",
    "average_try": 1.7508,
    "solvedtags": [
      {
        "bojTagId": 125,
        "key": "bruteforcing"
      },
      {
        "bojTagId": 33,
        "key": "greedy"
      },
      {
        "bojTagId": 102,
        "key": "implementation"
      },
      {
        "bojTagId": 158,
        "key": "string"
      }
    ],
    "lastupdate": 1687116861.570835
  },
  "2503": {
    "problemId": "2503",
    "problemLevel": 8,
    "problemName": "숫자 야구",
    "average_try": 2.116,
    "solvedtags": [
      {
        "bojTagId": 125,
        "key": "bruteforcing"
      },
      {
        "bojTagId": 102,
        "key": "implementation"
      }
    ],
    "lastupdate": 1687116861.570853
  },
  "1436": {
    "problemId": "1436",
    "problemLevel": 6,
    "problemName": "영화감독 숌",
    "average_try": 1.8075,
    "solvedtags": [
      {
        "bojTagId": 125,
        "key": "bruteforcing"
      }
    ],
    "lastupdate": 1687116861.570871
  },
  "1018": {
    "problemId": "1018",
    "problemLevel": 7,
    "problemName": "체스판 다시 칠하기",
    "average_try": 2.0298,
    "solvedtags": [
      {
        "bojTagId": 125,
        "key": "bruteforcing"
      }
    ],
    "lastupdate": 1687116861.570889
  },
  "7568": {
    "problemId": "7568",
    "problemLevel": 6,
    "problemName": "덩치",
    "average_try": 1.7884,
    "solvedtags": [
      {
        "bojTagId": 125,
        "key": "bruteforcing"
      },
      {
        "bojTagId": 102,
        "key": "implementation"
      }
    ],
    "lastupdate": 1687116861.570907
  },
  "2422": {
    "problemId": "2422",
    "problemLevel": 7,
    "problemName": "한윤정이 이탈리아에 가서 아이스크림을 사먹는데",
    "average_try": 2.4987,
    "solvedtags": [
      {
        "bojTagId": 125,
        "key": "bruteforcing"
      }
    ],
    "lastupdate": 1687116861.570925
  },
  "2435": {
    "problemId": "2435",
    "problemLevel": 5,
    "problemName": "기상청 인턴 신현수",
    "average_try": 2.1181,
    "solvedtags": [
      {
        "bojTagId": 125,
        "key": "bruteforcing"
      },
      {
        "bojTagId": 139,
        "key": "prefix_sum"
      }
    ],
    "lastupdate": 1687116861.570942
  },
  "2635": {
    "problemId": "2635",
    "problemLevel": 6,
    "problemName": "수 이어가기",
    "average_try": 2.6618,
    "solvedtags": [
      {
        "bojTagId": 125,
        "key": "bruteforcing"
      },
      {
        "bojTagId": 124,
        "key": "math"
      }
    ],
    "lastupdate": 1687116861.570977
  },
  "1059": {
    "problemId": "1059",
    "problemLevel": 7,
    "problemName": "좋은 구간",
    "average_try": 3.6006,
    "solvedtags": [
      {
        "bojTagId": 125,
        "key": "bruteforcing"
      },
      {
        "bojTagId": 124,
        "key": "math"
      },
      {
        "bojTagId": 97,
        "key": "sorting"
      }
    ],
    "lastupdate": 1687116861.570994
  },
  "5568": {
    "problemId": "5568",
    "problemLevel": 7,
    "problemName": "카드 놓기",
    "average_try": 1.542,
    "solvedtags": [
      {
        "bojTagId": 5,
        "key": "backtracking"
      },
      {
        "bojTagId": 125,
        "key": "bruteforcing"
      },
      {
        "bojTagId": 175,
        "key": "data_structures"
      },
      {
        "bojTagId": 136,
        "key": "hash_set"
      }
    ],
    "lastupdate": 1687116861.571011
  },
  "11170": {
    "problemId": "11170",
    "problemLevel": 5,
    "problemName": "0의 개수",
    "average_try": 1.2888,
    "solvedtags": [
      {
        "bojTagId": 125,
        "key": "bruteforcing"
      },
      {
        "bojTagId": 102,
        "key": "implementation"
      },
      {
        "bojTagId": 124,
        "key": "math"
      }
    ],
    "lastupdate": 1687116861.571029
  },
  "1251": {
    "problemId": "1251",
    "problemLevel": 6,
    "problemName": "단어 나누기",
    "average_try": 2.1633,
    "solvedtags": [
      {
        "bojTagId": 125,
        "key": "bruteforcing"
      },
      {
        "bojTagId": 102,
        "key": "implementation"
      },
      {
        "bojTagId": 97,
        "key": "sorting"
      },
      {
        "bojTagId": 158,
        "key": "string"
      }
    ],
    "lastupdate": 1687116861.571046
  },
  "14912": {
    "problemId": "14912",
    "problemLevel": 6,
    "problemName": "숫자 빈도수",
    "average_try": 1.2385,
    "solvedtags": [
      {
        "bojTagId": 125,
        "key": "bruteforcing"
      },
      {
        "bojTagId": 102,
        "key": "implementation"
      },
      {
        "bojTagId": 124,
        "key": "math"
      }
    ],
    "lastupdate": 1687116861.571063
  },
  "19947": {
    "problemId": "19947",
    "problemLevel": 6,
    "problemName": "투자의 귀재 배주형",
    "average_try": 2.7924,
    "solvedtags": [
      {
        "bojTagId": 125,
        "key": "bruteforcing"
      },
      {
        "bojTagId": 25,
        "key": "dp"
      }
    ],
    "lastupdate": 1687116861.571097
  },
  "1359": {
    "problemId": "1359",
    "problemLevel": 7,
    "problemName": "복권",
    "average_try": 2.4223,
    "solvedtags": [
      {
        "bojTagId": 125,
        "key": "bruteforcing"
      },
      {
        "bojTagId": 6,
        "key": "combinatorics"
      },
      {
        "bojTagId": 124,
        "key": "math"
      },
      {
        "bojTagId": 177,
        "key": "probability"
      }
    ],
    "lastupdate": 1687116861.571114
  },
  "15779": {
    "problemId": "15779",
    "problemLevel": 6,
    "problemName": "Zigzag",
    "average_try": 2.3429,
    "solvedtags": [
      {
        "bojTagId": 125,
        "key": "bruteforcing"
      },
      {
        "bojTagId": 102,
        "key": "implementation"
      }
    ],
    "lastupdate": 1687116861.571132
  },
  "18511": {
    "problemId": "18511",
    "problemLevel": 6,
    "problemName": "큰 수 구성하기",
    "average_try": 3.392,
    "solvedtags": [
      {
        "bojTagId": 125,
        "key": "bruteforcing"
      },
      {
        "bojTagId": 62,
        "key": "recursion"
      }
    ],
    "lastupdate": 1687116861.571149
  },
  "17484": {
    "problemId": "17484",
    "problemLevel": 8,
    "problemName": "진우의 달 여행 (Small)",
    "average_try": 1.6875,
    "solvedtags": [
      {
        "bojTagId": 125,
        "key": "bruteforcing"
      },
      {
        "bojTagId": 25,
        "key": "dp"
      }
    ],
    "lastupdate": 1687116861.571167
  },
  "9079": {
    "problemId": "9079",
    "problemLevel": 9,
    "problemName": "동전 게임",
    "average_try": 1.5362,
    "solvedtags": [
      {
        "bojTagId": 14,
        "key": "bitmask"
      },
      {
        "bojTagId": 125,
        "key": "bruteforcing"
      }
    ],
    "lastupdate": 1687116861.571184
  },
  "4096": {
    "problemId": "4096",
    "problemLevel": 7,
    "problemName": "팰린드로미터",
    "average_try": 1.8199,
    "solvedtags": [
      {
        "bojTagId": 125,
        "key": "bruteforcing"
      },
      {
        "bojTagId": 158,
        "key": "string"
      }
    ],
    "lastupdate": 1687116861.571202
  },
  "1065": {
    "problemId": "1065",
    "problemLevel": 7,
    "problemName": "한수",
    "average_try": 1.8513,
    "solvedtags": [
      {
        "bojTagId": 125,
        "key": "bruteforcing"
      }
    ],
    "lastupdate": 1687116861.571219
  },
  "1120": {
    "problemId": "1120",
    "problemLevel": 7,
    "problemName": "문자열",
    "average_try": 1.7527,
    "solvedtags": [
      {
        "bojTagId": 125,
        "key": "bruteforcing"
      },
      {
        "bojTagId": 158,
        "key": "string"
      }
    ],
    "lastupdate": 1687116861.571255
  },
  "3085": {
    "problemId": "3085",
    "problemLevel": 9,
    "problemName": "사탕 게임",
    "average_try": 3.0367,
    "solvedtags": [
      {
        "bojTagId": 125,
        "key": "bruteforcing"
      },
      {
        "bojTagId": 102,
        "key": "implementation"
      }
    ],
    "lastupdate": 1687116861.571273
  },
  "1543": {
    "problemId": "1543",
    "problemLevel": 7,
    "problemName": "문서 검색",
    "average_try": 2.3245,
    "solvedtags": [
      {
        "bojTagId": 125,
        "key": "bruteforcing"
      },
      {
        "bojTagId": 158,
        "key": "string"
      }
    ],
    "lastupdate": 1687116861.57129
  },
  "15970": {
    "problemId": "15970",
    "problemLevel": 7,
    "problemName": "화살표 그리기",
    "average_try": 1.9795,
    "solvedtags": [
      {
        "bojTagId": 125,
        "key": "bruteforcing"
      },
      {
        "bojTagId": 97,
        "key": "sorting"
      }
    ],
    "lastupdate": 1687116861.571308
  },
  "5671": {
    "problemId": "5671",
    "problemLevel": 6,
    "problemName": "호텔 방 번호",
    "average_try": 1.7382,
    "solvedtags": [
      {
        "bojTagId": 125,
        "key": "bruteforcing"
      },
      {
        "bojTagId": 124,
        "key": "math"
      }
    ],
    "lastupdate": 1687116861.571325
  },
  "16937": {
    "problemId": "16937",
    "problemLevel": 8,
    "problemName": "두 스티커",
    "average_try": 2.6201,
    "solvedtags": [
      {
        "bojTagId": 125,
        "key": "bruteforcing"
      },
      {
        "bojTagId": 100,
        "key": "geometry"
      },
      {
        "bojTagId": 102,
        "key": "implementation"
      }
    ],
    "lastupdate": 1687116861.571343
  },
  "5883": {
    "problemId": "5883",
    "problemLevel": 7,
    "problemName": "아이폰 9S",
    "average_try": 2.3548,
    "solvedtags": [
      {
        "bojTagId": 125,
        "key": "bruteforcing"
      },
      {
        "bojTagId": 102,
        "key": "implementation"
      }
    ],
    "lastupdate": 1687116861.57136
  },
  "16951": {
    "problemId": "16951",
    "problemLevel": 7,
    "problemName": "블록 놀이",
    "average_try": 3,
    "solvedtags": [
      {
        "bojTagId": 125,
        "key": "bruteforcing"
      }
    ],
    "lastupdate": 1687116861.571377
  },
  "1487": {
    "problemId": "1487",
    "problemLevel": 7,
    "problemName": "물건 팔기",
    "average_try": 2.3252,
    "solvedtags": [
      {
        "bojTagId": 125,
        "key": "bruteforcing"
      }
    ],
    "lastupdate": 1687116861.571394
  },
  "15270": {
    "problemId": "15270",
    "problemLevel": 9,
    "problemName": "친구 팰린드롬",
    "average_try": 3.2901,
    "solvedtags": [
      {
        "bojTagId": 5,
        "key": "backtracking"
      },
      {
        "bojTagId": 127,
        "key": "dfs"
      },
      {
        "bojTagId": 7,
        "key": "graphs"
      },
      {
        "bojTagId": 11,
        "key": "graph_traversal"
      }
    ],
    "lastupdate": 1687116861.571412
  },
  "11502": {
    "problemId": "11502",
    "problemLevel": 7,
    "problemName": "세 개의 소수 문제",
    "average_try": 1.6723,
    "solvedtags": [
      {
        "bojTagId": 125,
        "key": "bruteforcing"
      },
      {
        "bojTagId": 124,
        "key": "math"
      },
      {
        "bojTagId": 95,
        "key": "number_theory"
      },
      {
        "bojTagId": 9,
        "key": "primality_test"
      },
      {
        "bojTagId": 67,
        "key": "sieve"
      }
    ],
    "lastupdate": 1687116861.571447
  },
  "9996": {
    "problemId": "9996",
    "problemLevel": 8,
    "problemName": "한국이 그리울 땐 서버에 접속하지",
    "average_try": 3.7302,
    "solvedtags": [
      {
        "bojTagId": 63,
        "key": "regex"
      },
      {
        "bojTagId": 158,
        "key": "string"
      }
    ],
    "lastupdate": 1687116861.571464
  },
  "10472": {
    "problemId": "10472",
    "problemLevel": 10,
    "problemName": "십자뒤집기",
    "average_try": 2.3679,
    "solvedtags": [
      {
        "bojTagId": 126,
        "key": "bfs"
      },
      {
        "bojTagId": 125,
        "key": "bruteforcing"
      },
      {
        "bojTagId": 7,
        "key": "graphs"
      },
      {
        "bojTagId": 11,
        "key": "graph_traversal"
      }
    ],
    "lastupdate": 1687116861.571481
  },
  "1895": {
    "problemId": "1895",
    "problemLevel": 7,
    "problemName": "필터",
    "average_try": 1.3614,
    "solvedtags": [
      {
        "bojTagId": 125,
        "key": "bruteforcing"
      },
      {
        "bojTagId": 102,
        "key": "implementation"
      },
      {
        "bojTagId": 97,
        "key": "sorting"
      }
    ],
    "lastupdate": 1687116861.571499
  },
  "16439": {
    "problemId": "16439",
    "problemLevel": 7,
    "problemName": "치킨치킨치킨",
    "average_try": 1.3398,
    "solvedtags": [
      {
        "bojTagId": 125,
        "key": "bruteforcing"
      }
    ],
    "lastupdate": 1687116861.571516
  },
  "19949": {
    "problemId": "19949",
    "problemLevel": 9,
    "problemName": "영재의 시험",
    "average_try": 1.2481,
    "solvedtags": [
      {
        "bojTagId": 5,
        "key": "backtracking"
      },
      {
        "bojTagId": 125,
        "key": "bruteforcing"
      }
    ],
    "lastupdate": 1687116861.571534
  },
  "15728": {
    "problemId": "15728",
    "problemLevel": 8,
    "problemName": "에리 - 카드",
    "average_try": 2.7917,
    "solvedtags": [
      {
        "bojTagId": 125,
        "key": "bruteforcing"
      },
      {
        "bojTagId": 102,
        "key": "implementation"
      }
    ],
    "lastupdate": 1687116861.571551
  },
  "16508": {
    "problemId": "16508",
    "problemLevel": 8,
    "problemName": "전공책",
    "average_try": 2.4436,
    "solvedtags": [
      {
        "bojTagId": 14,
        "key": "bitmask"
      },
      {
        "bojTagId": 125,
        "key": "bruteforcing"
      }
    ],
    "lastupdate": 1687116861.571568
  },
  "1503": {
    "problemId": "1503",
    "problemLevel": 9,
    "problemName": "세 수 고르기",
    "average_try": 4.8415,
    "solvedtags": [
      {
        "bojTagId": 125,
        "key": "bruteforcing"
      }
    ],
    "lastupdate": 1687116861.571585
  },
  "14620": {
    "problemId": "14620",
    "problemLevel": 9,
    "problemName": "꽃길",
    "average_try": 1.9598,
    "solvedtags": [
      {
        "bojTagId": 125,
        "key": "bruteforcing"
      }
    ],
    "lastupdate": 1687116861.571602
  },
  "12919": {
    "problemId": "12919",
    "problemLevel": 11,
    "problemName": "A와 B 2",
    "average_try": 3.1179,
    "solvedtags": [
      {
        "bojTagId": 125,
        "key": "bruteforcing"
      },
      {
        "bojTagId": 62,
        "key": "recursion"
      },
      {
        "bojTagId": 158,
        "key": "string"
      }
    ],
    "lastupdate": 1687116861.571619
  },
  "1421": {
    "problemId": "1421",
    "problemLevel": 9,
    "problemName": "나무꾼 이다솜",
    "average_try": 4.4354,
    "solvedtags": [
      {
        "bojTagId": 125,
        "key": "bruteforcing"
      },
      {
        "bojTagId": 102,
        "key": "implementation"
      }
    ],
    "lastupdate": 1687116861.571636
  },
  "1411": {
    "problemId": "1411",
    "problemLevel": 9,
    "problemName": "비슷한 단어",
    "average_try": 1.662,
    "solvedtags": [
      {
        "bojTagId": 125,
        "key": "bruteforcing"
      },
      {
        "bojTagId": 158,
        "key": "string"
      }
    ],
    "lastupdate": 1687116861.571654
  },
  "1548": {
    "problemId": "1548",
    "problemLevel": 11,
    "problemName": "부분 삼각 수열",
    "average_try": 2.4712,
    "solvedtags": [
      {
        "bojTagId": 125,
        "key": "bruteforcing"
      },
      {
        "bojTagId": 33,
        "key": "greedy"
      },
      {
        "bojTagId": 97,
        "key": "sorting"
      }
    ],
    "lastupdate": 1687116861.571671
  },
  "1254": {
    "problemId": "1254",
    "problemLevel": 9,
    "problemName": "팰린드롬 만들기",
    "average_try": 2.2116,
    "solvedtags": [
      {
        "bojTagId": 125,
        "key": "bruteforcing"
      },
      {
        "bojTagId": 158,
        "key": "string"
      }
    ],
    "lastupdate": 1687116861.571688
  },
  "2961": {
    "problemId": "2961",
    "problemLevel": 9,
    "problemName": "도영이가 만든 맛있는 음식",
    "average_try": 1.8853,
    "solvedtags": [
      {
        "bojTagId": 5,
        "key": "backtracking"
      },
      {
        "bojTagId": 14,
        "key": "bitmask"
      },
      {
        "bojTagId": 125,
        "key": "bruteforcing"
      }
    ],
    "lastupdate": 1687116861.571705
  },
  "15661": {
    "problemId": "15661",
    "problemLevel": 10,
    "problemName": "링크와 스타트",
    "average_try": 2.2279,
    "solvedtags": [
      {
        "bojTagId": 5,
        "key": "backtracking"
      },
      {
        "bojTagId": 14,
        "key": "bitmask"
      },
      {
        "bojTagId": 125,
        "key": "bruteforcing"
      }
    ],
    "lastupdate": 1687116861.571722
  },
  "1527": {
    "problemId": "1527",
    "problemLevel": 10,
    "problemName": "금민수의 개수",
    "average_try": 2.517,
    "solvedtags": [
      {
        "bojTagId": 125,
        "key": "bruteforcing"
      }
    ],
    "lastupdate": 1687116861.57174
  },
  "17610": {
    "problemId": "17610",
    "problemLevel": 10,
    "problemName": "양팔저울",
    "average_try": 2.3996,
    "solvedtags": [
      {
        "bojTagId": 125,
        "key": "bruteforcing"
      }
    ],
    "lastupdate": 1687116861.571758
  },
  "16943": {
    "problemId": "16943",
    "problemLevel": 10,
    "problemName": "숫자 재배치",
    "average_try": 2.2147,
    "solvedtags": [
      {
        "bojTagId": 5,
        "key": "backtracking"
      },
      {
        "bojTagId": 125,
        "key": "bruteforcing"
      },
      {
        "bojTagId": 6,
        "key": "combinatorics"
      },
      {
        "bojTagId": 124,
        "key": "math"
      }
    ],
    "lastupdate": 1687116861.571776
  },
  "1025": {
    "problemId": "1025",
    "problemLevel": 11,
    "problemName": "제곱수 찾기",
    "average_try": 3.0419,
    "solvedtags": [
      {
        "bojTagId": 125,
        "key": "bruteforcing"
      }
    ],
    "lastupdate": 1687116861.571793
  },
  "17085": {
    "problemId": "17085",
    "problemLevel": 11,
    "problemName": "십자가 2개 놓기",
    "average_try": 2.9175,
    "solvedtags": [
      {
        "bojTagId": 125,
        "key": "bruteforcing"
      },
      {
        "bojTagId": 102,
        "key": "implementation"
      }
    ],
    "lastupdate": 1687116861.571811
  },
  "14500": {
    "problemId": "14500",
    "problemLevel": 12,
    "problemName": "테트로미노",
    "average_try": 2.7827,
    "solvedtags": [
      {
        "bojTagId": 125,
        "key": "bruteforcing"
      },
      {
        "bojTagId": 102,
        "key": "implementation"
      }
    ],
    "lastupdate": 1687116861.571828
  },
  "15686": {
    "problemId": "15686",
    "problemLevel": 11,
    "problemName": "치킨 배달",
    "average_try": 2.1945,
    "solvedtags": [
      {
        "bojTagId": 5,
        "key": "backtracking"
      },
      {
        "bojTagId": 125,
        "key": "bruteforcing"
      },
      {
        "bojTagId": 102,
        "key": "implementation"
      }
    ],
    "lastupdate": 1687116861.571846
  },
  "1107": {
    "problemId": "1107",
    "problemLevel": 11,
    "problemName": "리모컨",
    "average_try": 4.3687,
    "solvedtags": [
      {
        "bojTagId": 125,
        "key": "bruteforcing"
      }
    ],
    "lastupdate": 1687116861.571863
  },
  "17471": {
    "problemId": "17471",
    "problemLevel": 12,
    "problemName": "게리맨더링",
    "average_try": 2.5047,
    "solvedtags": [
      {
        "bojTagId": 126,
        "key": "bfs"
      },
      {
        "bojTagId": 125,
        "key": "bruteforcing"
      },
      {
        "bojTagId": 6,
        "key": "combinatorics"
      },
      {
        "bojTagId": 127,
        "key": "dfs"
      },
      {
        "bojTagId": 7,
        "key": "graphs"
      },
      {
        "bojTagId": 11,
        "key": "graph_traversal"
      },
      {
        "bojTagId": 124,
        "key": "math"
      }
    ],
    "lastupdate": 1687116861.571881
  },
  "14225": {
    "problemId": "14225",
    "problemLevel": 10,
    "problemName": "부분수열의 합",
    "average_try": 2.2961,
    "solvedtags": [
      {
        "bojTagId": 125,
        "key": "bruteforcing"
      }
    ],
    "lastupdate": 1687116861.571916
  },
  "1034": {
    "problemId": "1034",
    "problemLevel": 12,
    "problemName": "램프",
    "average_try": 2.4413,
    "solvedtags": [
      {
        "bojTagId": 109,
        "key": "ad_hoc"
      },
      {
        "bojTagId": 125,
        "key": "bruteforcing"
      }
    ],
    "lastupdate": 1687116861.571933
  },
  "16637": {
    "problemId": "16637",
    "problemLevel": 13,
    "problemName": "괄호 추가하기",
    "average_try": 2.4768,
    "solvedtags": [
      {
        "bojTagId": 125,
        "key": "bruteforcing"
      }
    ],
    "lastupdate": 1687116861.571951
  },
  "14391": {
    "problemId": "14391",
    "problemLevel": 13,
    "problemName": "종이 조각",
    "average_try": 1.8102,
    "solvedtags": [
      {
        "bojTagId": 14,
        "key": "bitmask"
      },
      {
        "bojTagId": 125,
        "key": "bruteforcing"
      }
    ],
    "lastupdate": 1687116861.571968
  },
  "16986": {
    "problemId": "16986",
    "problemLevel": 13,
    "problemName": "인싸들의 가위바위보",
    "average_try": 2.3536,
    "solvedtags": [
      {
        "bojTagId": 5,
        "key": "backtracking"
      },
      {
        "bojTagId": 125,
        "key": "bruteforcing"
      },
      {
        "bojTagId": 102,
        "key": "implementation"
      }
    ],
    "lastupdate": 1687116861.572003
  },
  "1711": {
    "problemId": "1711",
    "problemLevel": 11,
    "problemName": "직각삼각형",
    "average_try": 3.0578,
    "solvedtags": [
      {
        "bojTagId": 125,
        "key": "bruteforcing"
      },
      {
        "bojTagId": 100,
        "key": "geometry"
      },
      {
        "bojTagId": 60,
        "key": "pythagoras"
      }
    ],
    "lastupdate": 1687116861.572021
  },
  "1581": {
    "problemId": "1581",
    "problemLevel": 12,
    "problemName": "락스타 락동호",
    "average_try": 3.2476,
    "solvedtags": [
      {
        "bojTagId": 137,
        "key": "case_work"
      }
    ],
    "lastupdate": 1687116861.572038
  },
  "21278": {
    "problemId": "21278",
    "problemLevel": 11,
    "problemName": "호석이 두 마리 치킨",
    "average_try": 2.0518,
    "solvedtags": [
      {
        "bojTagId": 126,
        "key": "bfs"
      },
      {
        "bojTagId": 125,
        "key": "bruteforcing"
      },
      {
        "bojTagId": 31,
        "key": "floyd_warshall"
      },
      {
        "bojTagId": 7,
        "key": "graphs"
      },
      {
        "bojTagId": 11,
        "key": "graph_traversal"
      }
    ],
    "lastupdate": 1687116861.572055
  },
  "21315": {
    "problemId": "21315",
    "problemLevel": 11,
    "problemName": "카드 섞기",
    "average_try": 2.1667,
    "solvedtags": [
      {
        "bojTagId": 125,
        "key": "bruteforcing"
      },
      {
        "bojTagId": 102,
        "key": "implementation"
      },
      {
        "bojTagId": 141,
        "key": "simulation"
      }
    ],
    "lastupdate": 1687116861.572073
  },
  "2304": {
    "problemId": "2304",
    "problemLevel": 9,
    "problemName": "창고 다각형",
    "average_try": 2.4046,
    "solvedtags": [
      {
        "bojTagId": 125,
        "key": "bruteforcing"
      },
      {
        "bojTagId": 175,
        "key": "data_structures"
      },
      {
        "bojTagId": 71,
        "key": "stack"
      }
    ],
    "lastupdate": 1687116861.572091
  },
  "21943": {
    "problemId": "21943",
    "problemLevel": 14,
    "problemName": "연산 최대로",
    "average_try": 1.9293,
    "solvedtags": [
      {
        "bojTagId": 125,
        "key": "bruteforcing"
      },
      {
        "bojTagId": 33,
        "key": "greedy"
      }
    ],
    "lastupdate": 1687116861.572108
  },
  "22944": {
    "problemId": "22944",
    "problemLevel": 13,
    "problemName": "죽음의 비",
    "average_try": 6.0092,
    "solvedtags": [
      {
        "bojTagId": 5,
        "key": "backtracking"
      },
      {
        "bojTagId": 126,
        "key": "bfs"
      },
      {
        "bojTagId": 125,
        "key": "bruteforcing"
      },
      {
        "bojTagId": 7,
        "key": "graphs"
      },
      {
        "bojTagId": 11,
        "key": "graph_traversal"
      }
    ],
    "lastupdate": 1687116861.572143
  },
  "22947": {
    "problemId": "22947",
    "problemLevel": 14,
    "problemName": "실행 시간",
    "average_try": 3.0571,
    "solvedtags": [
      {
        "bojTagId": 125,
        "key": "bruteforcing"
      },
      {
        "bojTagId": 7,
        "key": "graphs"
      },
      {
        "bojTagId": 78,
        "key": "topological_sorting"
      }
    ],
    "lastupdate": 1687116861.572161
  },
  "10828": {
    "problemId": "10828",
    "problemLevel": 7,
    "problemName": "스택",
    "average_try": 2.6806,
    "solvedtags": [
      {
        "bojTagId": 175,
        "key": "data_structures"
      },
      {
        "bojTagId": 102,
        "key": "implementation"
      },
      {
        "bojTagId": 71,
        "key": "stack"
      }
    ],
    "lastupdate": 1687116861.573072
  },
  "9012": {
    "problemId": "9012",
    "problemLevel": 7,
    "problemName": "괄호",
    "average_try": 2.2051,
    "solvedtags": [
      {
        "bojTagId": 175,
        "key": "data_structures"
      },
      {
        "bojTagId": 71,
        "key": "stack"
      },
      {
        "bojTagId": 158,
        "key": "string"
      }
    ],
    "lastupdate": 1687116861.573097
  },
  "1874": {
    "problemId": "1874",
    "problemLevel": 9,
    "problemName": "스택 수열",
    "average_try": 2.6816,
    "solvedtags": [
      {
        "bojTagId": 175,
        "key": "data_structures"
      },
      {
        "bojTagId": 71,
        "key": "stack"
      }
    ],
    "lastupdate": 1687116861.573128
  },
  "1935": {
    "problemId": "1935",
    "problemLevel": 8,
    "problemName": "후위 표기식2",
    "average_try": 2.0606,
    "solvedtags": [
      {
        "bojTagId": 175,
        "key": "data_structures"
      },
      {
        "bojTagId": 71,
        "key": "stack"
      }
    ],
    "lastupdate": 1687116861.573147
  },
  "10799": {
    "problemId": "10799",
    "problemLevel": 9,
    "problemName": "쇠막대기",
    "average_try": 1.5481,
    "solvedtags": [
      {
        "bojTagId": 175,
        "key": "data_structures"
      },
      {
        "bojTagId": 71,
        "key": "stack"
      }
    ],
    "lastupdate": 1687116861.573166
  },
  "2504": {
    "problemId": "2504",
    "problemLevel": 10,
    "problemName": "괄호의 값",
    "average_try": 3.3647,
    "solvedtags": [
      {
        "bojTagId": 175,
        "key": "data_structures"
      },
      {
        "bojTagId": 102,
        "key": "implementation"
      },
      {
        "bojTagId": 71,
        "key": "stack"
      }
    ],
    "lastupdate": 1687116861.573185
  },
  "2800": {
    "problemId": "2800",
    "problemLevel": 11,
    "problemName": "괄호 제거",
    "average_try": 2.7623,
    "solvedtags": [
      {
        "bojTagId": 125,
        "key": "bruteforcing"
      },
      {
        "bojTagId": 175,
        "key": "data_structures"
      },
      {
        "bojTagId": 71,
        "key": "stack"
      },
      {
        "bojTagId": 158,
        "key": "string"
      }
    ],
    "lastupdate": 1687116861.573203
  },
  "2493": {
    "problemId": "2493",
    "problemLevel": 11,
    "problemName": "탑",
    "average_try": 3.168,
    "solvedtags": [
      {
        "bojTagId": 175,
        "key": "data_structures"
      },
      {
        "bojTagId": 71,
        "key": "stack"
      }
    ],
    "lastupdate": 1687116861.573222
  },
  "1918": {
    "problemId": "1918",
    "problemLevel": 14,
    "problemName": "후위 표기식",
    "average_try": 2.7578,
    "solvedtags": [
      {
        "bojTagId": 175,
        "key": "data_structures"
      },
      {
        "bojTagId": 71,
        "key": "stack"
      }
    ],
    "lastupdate": 1687116861.573241
  },
  "18258": {
    "problemId": "18258",
    "problemLevel": 7,
    "problemName": "큐 2",
    "average_try": 3.1355,
    "solvedtags": [
      {
        "bojTagId": 175,
        "key": "data_structures"
      },
      {
        "bojTagId": 72,
        "key": "queue"
      }
    ],
    "lastupdate": 1687116861.573259
  },
  "1158": {
    "problemId": "1158",
    "problemLevel": 7,
    "problemName": "요세푸스 문제",
    "average_try": 2.0646,
    "solvedtags": [
      {
        "bojTagId": 175,
        "key": "data_structures"
      },
      {
        "bojTagId": 102,
        "key": "implementation"
      },
      {
        "bojTagId": 72,
        "key": "queue"
      }
    ],
    "lastupdate": 1687116861.573278
  },
  "2164": {
    "problemId": "2164",
    "problemLevel": 7,
    "problemName": "카드2",
    "average_try": 1.9628,
    "solvedtags": [
      {
        "bojTagId": 175,
        "key": "data_structures"
      },
      {
        "bojTagId": 72,
        "key": "queue"
      }
    ],
    "lastupdate": 1687116861.573296
  },
  "1966": {
    "problemId": "1966",
    "problemLevel": 8,
    "problemName": "프린터 큐",
    "average_try": 1.7218,
    "solvedtags": [
      {
        "bojTagId": 175,
        "key": "data_structures"
      },
      {
        "bojTagId": 102,
        "key": "implementation"
      },
      {
        "bojTagId": 72,
        "key": "queue"
      },
      {
        "bojTagId": 141,
        "key": "simulation"
      }
    ],
    "lastupdate": 1687116861.573314
  },
  "10866": {
    "problemId": "10866",
    "problemLevel": 7,
    "problemName": "덱",
    "average_try": 1.7848,
    "solvedtags": [
      {
        "bojTagId": 175,
        "key": "data_structures"
      },
      {
        "bojTagId": 73,
        "key": "deque"
      },
      {
        "bojTagId": 102,
        "key": "implementation"
      }
    ],
    "lastupdate": 1687116861.573332
  },
  "2346": {
    "problemId": "2346",
    "problemLevel": 8,
    "problemName": "풍선 터뜨리기",
    "average_try": 2.3584,
    "solvedtags": [
      {
        "bojTagId": 175,
        "key": "data_structures"
      },
      {
        "bojTagId": 73,
        "key": "deque"
      }
    ],
    "lastupdate": 1687116861.57335
  },
  "10845": {
    "problemId": "10845",
    "problemLevel": 7,
    "problemName": "큐",
    "average_try": 2.0449,
    "solvedtags": [
      {
        "bojTagId": 175,
        "key": "data_structures"
      },
      {
        "bojTagId": 72,
        "key": "queue"
      }
    ],
    "lastupdate": 1687116861.573369
  },
  "4949": {
    "problemId": "4949",
    "problemLevel": 7,
    "problemName": "균형잡힌 세상",
    "average_try": 3.0872,
    "solvedtags": [
      {
        "bojTagId": 175,
        "key": "data_structures"
      },
      {
        "bojTagId": 71,
        "key": "stack"
      },
      {
        "bojTagId": 158,
        "key": "string"
      }
    ],
    "lastupdate": 1687116861.573388
  },
  "3986": {
    "problemId": "3986",
    "problemLevel": 7,
    "problemName": "좋은 단어",
    "average_try": 1.8096,
    "solvedtags": [
      {
        "bojTagId": 175,
        "key": "data_structures"
      },
      {
        "bojTagId": 71,
        "key": "stack"
      }
    ],
    "lastupdate": 1687116861.573406
  },
  "1021": {
    "problemId": "1021",
    "problemLevel": 8,
    "problemName": "회전하는 큐",
    "average_try": 1.6471,
    "solvedtags": [
      {
        "bojTagId": 175,
        "key": "data_structures"
      },
      {
        "bojTagId": 73,
        "key": "deque"
      }
    ],
    "lastupdate": 1687116861.573424
  },
  "5397": {
    "problemId": "5397",
    "problemLevel": 9,
    "problemName": "키로거",
    "average_try": 3.8127,
    "solvedtags": [
      {
        "bojTagId": 175,
        "key": "data_structures"
      },
      {
        "bojTagId": 154,
        "key": "linked_list"
      },
      {
        "bojTagId": 71,
        "key": "stack"
      }
    ],
    "lastupdate": 1687116861.573443
  },
  "18115": {
    "problemId": "18115",
    "problemLevel": 8,
    "problemName": "카드 놓기",
    "average_try": 1.8705,
    "solvedtags": [
      {
        "bojTagId": 175,
        "key": "data_structures"
      },
      {
        "bojTagId": 73,
        "key": "deque"
      }
    ],
    "lastupdate": 1687116861.573462
  },
  "5430": {
    "problemId": "5430",
    "problemLevel": 11,
    "problemName": "AC",
    "average_try": 5.0054,
    "solvedtags": [
      {
        "bojTagId": 73,
        "key": "deque"
      },
      {
        "bojTagId": 96,
        "key": "parsing"
      },
      {
        "bojTagId": 102,
        "key": "implementation"
      },
      {
        "bojTagId": 158,
        "key": "string"
      },
      {
        "bojTagId": 175,
        "key": "data_structures"
      }
    ],
    "lastupdate": 1687116861.57348
  },
  "1863": {
    "problemId": "1863",
    "problemLevel": 12,
    "problemName": "스카이라인 쉬운거",
    "average_try": 2.4643,
    "solvedtags": [
      {
        "bojTagId": 175,
        "key": "data_structures"
      },
      {
        "bojTagId": 71,
        "key": "stack"
      }
    ],
    "lastupdate": 1687116861.573499
  },
  "22866": {
    "problemId": "22866",
    "problemLevel": 13,
    "problemName": "탑 보기",
    "average_try": 3.2794,
    "solvedtags": [
      {
        "bojTagId": 175,
        "key": "data_structures"
      },
      {
        "bojTagId": 71,
        "key": "stack"
      }
    ],
    "lastupdate": 1687116861.573517
  },
  "22942": {
    "problemId": "22942",
    "problemLevel": 12,
    "problemName": "데이터 체커",
    "average_try": 3.1564,
    "solvedtags": [
      {
        "bojTagId": 175,
        "key": "data_structures"
      },
      {
        "bojTagId": 100,
        "key": "geometry"
      },
      {
        "bojTagId": 97,
        "key": "sorting"
      },
      {
        "bojTagId": 71,
        "key": "stack"
      },
      {
        "bojTagId": 106,
        "key": "sweeping"
      }
    ],
    "lastupdate": 1687116861.573535
  },
  "11279": {
    "problemId": "11279",
    "problemLevel": 9,
    "problemName": "최대 힙",
    "average_try": 2.0918,
    "solvedtags": [
      {
        "bojTagId": 175,
        "key": "data_structures"
      },
      {
        "bojTagId": 59,
        "key": "priority_queue"
      }
    ],
    "lastupdate": 1687116861.57397
  },
  "11286": {
    "problemId": "11286",
    "problemLevel": 10,
    "problemName": "절댓값 힙",
    "average_try": 1.7746,
    "solvedtags": [
      {
        "bojTagId": 175,
        "key": "data_structures"
      },
      {
        "bojTagId": 59,
        "key": "priority_queue"
      }
    ],
    "lastupdate": 1687116861.573989
  },
  "7662": {
    "problemId": "7662",
    "problemLevel": 12,
    "problemName": "이중 우선순위 큐",
    "average_try": 4.5849,
    "solvedtags": [
      {
        "bojTagId": 175,
        "key": "data_structures"
      },
      {
        "bojTagId": 59,
        "key": "priority_queue"
      },
      {
        "bojTagId": 74,
        "key": "tree_set"
      }
    ],
    "lastupdate": 1687116861.574008
  },
  "2075": {
    "problemId": "2075",
    "problemLevel": 9,
    "problemName": "N번째 큰 수",
    "average_try": 2.5602,
    "solvedtags": [
      {
        "bojTagId": 175,
        "key": "data_structures"
      },
      {
        "bojTagId": 59,
        "key": "priority_queue"
      },
      {
        "bojTagId": 97,
        "key": "sorting"
      }
    ],
    "lastupdate": 1687116861.574038
  },
  "2696": {
    "problemId": "2696",
    "problemLevel": 14,
    "problemName": "중앙값 구하기",
    "average_try": 2.0231,
    "solvedtags": [
      {
        "bojTagId": 175,
        "key": "data_structures"
      },
      {
        "bojTagId": 59,
        "key": "priority_queue"
      }
    ],
    "lastupdate": 1687116861.574086
  },
  "9375": {
    "problemId": "9375",
    "problemLevel": 8,
    "problemName": "패션왕 신해빈",
    "average_try": 1.8229,
    "solvedtags": [
      {
        "bojTagId": 6,
        "key": "combinatorics"
      },
      {
        "bojTagId": 175,
        "key": "data_structures"
      },
      {
        "bojTagId": 136,
        "key": "hash_set"
      },
      {
        "bojTagId": 124,
        "key": "math"
      }
    ],
    "lastupdate": 1687116861.574104
  },
  "1927": {
    "problemId": "1927",
    "problemLevel": 9,
    "problemName": "최소 힙",
    "average_try": 2.0392,
    "solvedtags": [
      {
        "bojTagId": 175,
        "key": "data_structures"
      },
      {
        "bojTagId": 59,
        "key": "priority_queue"
      }
    ],
    "lastupdate": 1687116861.574122
  },
  "12764": {
    "problemId": "12764",
    "problemLevel": 13,
    "problemName": "싸지방에 간 준하",
    "average_try": 3.4046,
    "solvedtags": [
      {
        "bojTagId": 175,
        "key": "data_structures"
      },
      {
        "bojTagId": 102,
        "key": "implementation"
      },
      {
        "bojTagId": 59,
        "key": "priority_queue"
      },
      {
        "bojTagId": 141,
        "key": "simulation"
      }
    ],
    "lastupdate": 1687116861.574177
  },
  "1655": {
    "problemId": "1655",
    "problemLevel": 14,
    "problemName": "가운데를 말해요",
    "average_try": 3.2957,
    "solvedtags": [
      {
        "bojTagId": 175,
        "key": "data_structures"
      },
      {
        "bojTagId": 59,
        "key": "priority_queue"
      }
    ],
    "lastupdate": 1687116861.574195
  },
  "2776": {
    "problemId": "2776",
    "problemLevel": 7,
    "problemName": "암기왕",
    "average_try": 3.2523,
    "solvedtags": [
      {
        "bojTagId": 12,
        "key": "binary_search"
      },
      {
        "bojTagId": 175,
        "key": "data_structures"
      },
      {
        "bojTagId": 136,
        "key": "hash_set"
      },
      {
        "bojTagId": 97,
        "key": "sorting"
      }
    ],
    "lastupdate": 1687116861.574213
  },
  "1269": {
    "problemId": "1269",
    "problemLevel": 7,
    "problemName": "대칭 차집합",
    "average_try": 1.569,
    "solvedtags": [
      {
        "bojTagId": 175,
        "key": "data_structures"
      },
      {
        "bojTagId": 136,
        "key": "hash_set"
      },
      {
        "bojTagId": 74,
        "key": "tree_set"
      }
    ],
    "lastupdate": 1687116861.57423
  },
  "10546": {
    "problemId": "10546",
    "problemLevel": 7,
    "problemName": "배부른 마라토너",
    "average_try": 2.2212,
    "solvedtags": [
      {
        "bojTagId": 175,
        "key": "data_structures"
      },
      {
        "bojTagId": 136,
        "key": "hash_set"
      }
    ],
    "lastupdate": 1687116861.574248
  },
  "1302": {
    "problemId": "1302",
    "problemLevel": 7,
    "problemName": "베스트셀러",
    "average_try": 1.9093,
    "solvedtags": [
      {
        "bojTagId": 175,
        "key": "data_structures"
      },
      {
        "bojTagId": 136,
        "key": "hash_set"
      },
      {
        "bojTagId": 97,
        "key": "sorting"
      },
      {
        "bojTagId": 158,
        "key": "string"
      }
    ],
    "lastupdate": 1687116861.574267
  },
  "21939": {
    "problemId": "21939",
    "problemLevel": 12,
    "problemName": "문제 추천 시스템 Version 1",
    "average_try": 3.3032,
    "solvedtags": [
      {
        "bojTagId": 175,
        "key": "data_structures"
      },
      {
        "bojTagId": 59,
        "key": "priority_queue"
      },
      {
        "bojTagId": 74,
        "key": "tree_set"
      }
    ],
    "lastupdate": 1687116861.574285
  },
  "21942": {
    "problemId": "21942",
    "problemLevel": 14,
    "problemName": "부품 대여장",
    "average_try": 4.1878,
    "solvedtags": [
      {
        "bojTagId": 175,
        "key": "data_structures"
      },
      {
        "bojTagId": 136,
        "key": "hash_set"
      },
      {
        "bojTagId": 102,
        "key": "implementation"
      },
      {
        "bojTagId": 96,
        "key": "parsing"
      },
      {
        "bojTagId": 158,
        "key": "string"
      }
    ],
    "lastupdate": 1687116861.574302
  },
  "21944": {
    "problemId": "21944",
    "problemLevel": 14,
    "problemName": "문제 추천 시스템 Version 2",
    "average_try": 3.6148,
    "solvedtags": [
      {
        "bojTagId": 175,
        "key": "data_structures"
      },
      {
        "bojTagId": 74,
        "key": "tree_set"
      }
    ],
    "lastupdate": 1687116861.57432
  },
  "1717": {
    "problemId": "1717",
    "problemLevel": 11,
    "problemName": "집합의 표현",
    "average_try": 3.5593,
    "solvedtags": [
      {
        "bojTagId": 175,
        "key": "data_structures"
      },
      {
        "bojTagId": 81,
        "key": "disjoint_set"
      }
    ],
    "lastupdate": 1687116861.574673
  },
  "1976": {
    "problemId": "1976",
    "problemLevel": 12,
    "problemName": "여행 가자",
    "average_try": 2.6995,
    "solvedtags": [
      {
        "bojTagId": 175,
        "key": "data_structures"
      },
      {
        "bojTagId": 81,
        "key": "disjoint_set"
      },
      {
        "bojTagId": 7,
        "key": "graphs"
      },
      {
        "bojTagId": 11,
        "key": "graph_traversal"
      }
    ],
    "lastupdate": 1687116861.574698
  },
  "16562": {
    "problemId": "16562",
    "problemLevel": 12,
    "problemName": "친구비",
    "average_try": 2.3808,
    "solvedtags": [
      {
        "bojTagId": 175,
        "key": "data_structures"
      },
      {
        "bojTagId": 81,
        "key": "disjoint_set"
      },
      {
        "bojTagId": 7,
        "key": "graphs"
      },
      {
        "bojTagId": 11,
        "key": "graph_traversal"
      }
    ],
    "lastupdate": 1687116861.574719
  },
  "4195": {
    "problemId": "4195",
    "problemLevel": 14,
    "problemName": "친구 네트워크",
    "average_try": 3.8311,
    "solvedtags": [
      {
        "bojTagId": 175,
        "key": "data_structures"
      },
      {
        "bojTagId": 81,
        "key": "disjoint_set"
      },
      {
        "bojTagId": 136,
        "key": "hash_set"
      }
    ],
    "lastupdate": 1687116861.574737
  },
  "10775": {
    "problemId": "10775",
    "problemLevel": 14,
    "problemName": "공항",
    "average_try": 2.8524,
    "solvedtags": [
      {
        "bojTagId": 175,
        "key": "data_structures"
      },
      {
        "bojTagId": 81,
        "key": "disjoint_set"
      },
      {
        "bojTagId": 33,
        "key": "greedy"
      }
    ],
    "lastupdate": 1687116861.574765
  },
  "20040": {
    "problemId": "20040",
    "problemLevel": 12,
    "problemName": "사이클 게임",
    "average_try": 1.9909,
    "solvedtags": [
      {
        "bojTagId": 175,
        "key": "data_structures"
      },
      {
        "bojTagId": 81,
        "key": "disjoint_set"
      }
    ],
    "lastupdate": 1687116861.574784
  },
  "11085": {
    "problemId": "11085",
    "problemLevel": 13,
    "problemName": "군사 이동",
    "average_try": 1.5909,
    "solvedtags": [
      {
        "bojTagId": 175,
        "key": "data_structures"
      },
      {
        "bojTagId": 81,
        "key": "disjoint_set"
      },
      {
        "bojTagId": 7,
        "key": "graphs"
      },
      {
        "bojTagId": 11,
        "key": "graph_traversal"
      }
    ],
    "lastupdate": 1687116861.574802
  },
  "17398": {
    "problemId": "17398",
    "problemLevel": 15,
    "problemName": "통신망 분할",
    "average_try": 2.9218,
    "solvedtags": [
      {
        "bojTagId": 175,
        "key": "data_structures"
      },
      {
        "bojTagId": 81,
        "key": "disjoint_set"
      }
    ],
    "lastupdate": 1687116861.57482
  },
  "17352": {
    "problemId": "17352",
    "problemLevel": 11,
    "problemName": "여러분의 다리가 되어 드리겠습니다!",
    "average_try": 1.9448,
    "solvedtags": [
      {
        "bojTagId": 175,
        "key": "data_structures"
      },
      {
        "bojTagId": 81,
        "key": "disjoint_set"
      },
      {
        "bojTagId": 7,
        "key": "graphs"
      },
      {
        "bojTagId": 11,
        "key": "graph_traversal"
      }
    ],
    "lastupdate": 1687116861.574838
  },
  "12893": {
    "problemId": "12893",
    "problemLevel": 12,
    "problemName": "적의 적",
    "average_try": 2.7386,
    "solvedtags": [
      {
        "bojTagId": 197,
        "key": "bipartite_graph"
      },
      {
        "bojTagId": 175,
        "key": "data_structures"
      },
      {
        "bojTagId": 81,
        "key": "disjoint_set"
      },
      {
        "bojTagId": 7,
        "key": "graphs"
      },
      {
        "bojTagId": 11,
        "key": "graph_traversal"
      }
    ],
    "lastupdate": 1687116861.574856
  },
  "1043": {
    "problemId": "1043",
    "problemLevel": 12,
    "problemName": "거짓말",
    "average_try": 2.2428,
    "solvedtags": [
      {
        "bojTagId": 175,
        "key": "data_structures"
      },
      {
        "bojTagId": 81,
        "key": "disjoint_set"
      },
      {
        "bojTagId": 7,
        "key": "graphs"
      },
      {
        "bojTagId": 11,
        "key": "graph_traversal"
      }
    ],
    "lastupdate": 1687116861.574875
  },
  "16168": {
    "problemId": "16168",
    "problemLevel": 12,
    "problemName": "퍼레이드",
    "average_try": 3.1168,
    "solvedtags": [
      {
        "bojTagId": 175,
        "key": "data_structures"
      },
      {
        "bojTagId": 81,
        "key": "disjoint_set"
      },
      {
        "bojTagId": 93,
        "key": "eulerian_path"
      },
      {
        "bojTagId": 7,
        "key": "graphs"
      },
      {
        "bojTagId": 11,
        "key": "graph_traversal"
      }
    ],
    "lastupdate": 1687116861.574893
  },
  "7511": {
    "problemId": "7511",
    "problemLevel": 11,
    "problemName": "소셜 네트워킹 어플리케이션",
    "average_try": 2.3897,
    "solvedtags": [
      {
        "bojTagId": 175,
        "key": "data_structures"
      },
      {
        "bojTagId": 81,
        "key": "disjoint_set"
      },
      {
        "bojTagId": 7,
        "key": "graphs"
      },
      {
        "bojTagId": 11,
        "key": "graph_traversal"
      }
    ],
    "lastupdate": 1687116861.57491
  },
  "3108": {
    "problemId": "3108",
    "problemLevel": 14,
    "problemName": "로고",
    "average_try": 3.2838,
    "solvedtags": [
      {
        "bojTagId": 175,
        "key": "data_structures"
      },
      {
        "bojTagId": 81,
        "key": "disjoint_set"
      },
      {
        "bojTagId": 100,
        "key": "geometry"
      }
    ],
    "lastupdate": 1687116861.574946
  },
  "15789": {
    "problemId": "15789",
    "problemLevel": 12,
    "problemName": "CTP 왕국은 한솔 왕국을 이길 수 있을까?",
    "average_try": 2.3412,
    "solvedtags": [
      {
        "bojTagId": 175,
        "key": "data_structures"
      },
      {
        "bojTagId": 81,
        "key": "disjoint_set"
      },
      {
        "bojTagId": 7,
        "key": "graphs"
      },
      {
        "bojTagId": 97,
        "key": "sorting"
      }
    ],
    "lastupdate": 1687116861.574963
  },
  "18116": {
    "problemId": "18116",
    "problemLevel": 12,
    "problemName": "로봇 조립",
    "average_try": 3.4403,
    "solvedtags": [
      {
        "bojTagId": 175,
        "key": "data_structures"
      },
      {
        "bojTagId": 81,
        "key": "disjoint_set"
      }
    ],
    "lastupdate": 1687116861.574981
  },
  "17090": {
    "problemId": "17090",
    "problemLevel": 13,
    "problemName": "미로 탈출하기",
    "average_try": 2.9683,
    "solvedtags": [
      {
        "bojTagId": 127,
        "key": "dfs"
      },
      {
        "bojTagId": 25,
        "key": "dp"
      },
      {
        "bojTagId": 7,
        "key": "graphs"
      },
      {
        "bojTagId": 11,
        "key": "graph_traversal"
      }
    ],
    "lastupdate": 1687116861.574999
  },
  "16724": {
    "problemId": "16724",
    "problemLevel": 13,
    "problemName": "피리 부는 사나이",
    "average_try": 2.3724,
    "solvedtags": [
      {
        "bojTagId": 175,
        "key": "data_structures"
      },
      {
        "bojTagId": 127,
        "key": "dfs"
      },
      {
        "bojTagId": 81,
        "key": "disjoint_set"
      },
      {
        "bojTagId": 7,
        "key": "graphs"
      },
      {
        "bojTagId": 11,
        "key": "graph_traversal"
      }
    ],
    "lastupdate": 1687116861.575017
  },
  "14595": {
    "problemId": "14595",
    "problemLevel": 13,
    "problemName": "동방 프로젝트 (Large)",
    "average_try": 2.7024,
    "solvedtags": [
      {
        "bojTagId": 175,
        "key": "data_structures"
      },
      {
        "bojTagId": 81,
        "key": "disjoint_set"
      },
      {
        "bojTagId": 106,
        "key": "sweeping"
      }
    ],
    "lastupdate": 1687116861.575035
  },
  "2630": {
    "problemId": "2630",
    "problemLevel": 9,
    "problemName": "색종이 만들기",
    "average_try": 1.444,
    "solvedtags": [
      {
        "bojTagId": 24,
        "key": "divide_and_conquer"
      },
      {
        "bojTagId": 62,
        "key": "recursion"
      }
    ],
    "lastupdate": 1687116861.575366
  },
  "4779": {
    "problemId": "4779",
    "problemLevel": 8,
    "problemName": "칸토어 집합",
    "average_try": 2.1907,
    "solvedtags": [
      {
        "bojTagId": 24,
        "key": "divide_and_conquer"
      },
      {
        "bojTagId": 62,
        "key": "recursion"
      }
    ],
    "lastupdate": 1687116861.57539
  },
  "1780": {
    "problemId": "1780",
    "problemLevel": 9,
    "problemName": "종이의 개수",
    "average_try": 1.6944,
    "solvedtags": [
      {
        "bojTagId": 24,
        "key": "divide_and_conquer"
      },
      {
        "bojTagId": 62,
        "key": "recursion"
      }
    ],
    "lastupdate": 1687116861.575411
  },
  "17829": {
    "problemId": "17829",
    "problemLevel": 9,
    "problemName": "222-풀링",
    "average_try": 1.3465,
    "solvedtags": [
      {
        "bojTagId": 24,
        "key": "divide_and_conquer"
      },
      {
        "bojTagId": 102,
        "key": "implementation"
      },
      {
        "bojTagId": 62,
        "key": "recursion"
      }
    ],
    "lastupdate": 1687116861.57543
  },
  "18222": {
    "problemId": "18222",
    "problemLevel": 9,
    "problemName": "투에-모스 문자열",
    "average_try": 2.5172,
    "solvedtags": [
      {
        "bojTagId": 24,
        "key": "divide_and_conquer"
      },
      {
        "bojTagId": 62,
        "key": "recursion"
      }
    ],
    "lastupdate": 1687116861.575449
  },
  "1802": {
    "problemId": "1802",
    "problemLevel": 10,
    "problemName": "종이 접기",
    "average_try": 2.7599,
    "solvedtags": [
      {
        "bojTagId": 109,
        "key": "ad_hoc"
      },
      {
        "bojTagId": 24,
        "key": "divide_and_conquer"
      }
    ],
    "lastupdate": 1687116861.575467
  },
  "2447": {
    "problemId": "2447",
    "problemLevel": 11,
    "problemName": "별 찍기 - 10",
    "average_try": 1.8346,
    "solvedtags": [
      {
        "bojTagId": 24,
        "key": "divide_and_conquer"
      },
      {
        "bojTagId": 62,
        "key": "recursion"
      }
    ],
    "lastupdate": 1687116861.575485
  },
  "1992": {
    "problemId": "1992",
    "problemLevel": 10,
    "problemName": "쿼드트리",
    "average_try": 1.6177,
    "solvedtags": [
      {
        "bojTagId": 24,
        "key": "divide_and_conquer"
      },
      {
        "bojTagId": 62,
        "key": "recursion"
      }
    ],
    "lastupdate": 1687116861.575502
  },
  "1074": {
    "problemId": "1074",
    "problemLevel": 10,
    "problemName": "Z",
    "average_try": 2.4875,
    "solvedtags": [
      {
        "bojTagId": 24,
        "key": "divide_and_conquer"
      },
      {
        "bojTagId": 62,
        "key": "recursion"
      }
    ],
    "lastupdate": 1687116861.57552
  },
  "5904": {
    "problemId": "5904",
    "problemLevel": 11,
    "problemName": "Moo 게임",
    "average_try": 2.8801,
    "solvedtags": [
      {
        "bojTagId": 24,
        "key": "divide_and_conquer"
      },
      {
        "bojTagId": 62,
        "key": "recursion"
      }
    ],
    "lastupdate": 1687116861.575538
  },
  "1493": {
    "problemId": "1493",
    "problemLevel": 13,
    "problemName": "박스 채우기",
    "average_try": 3.5423,
    "solvedtags": [
      {
        "bojTagId": 24,
        "key": "divide_and_conquer"
      },
      {
        "bojTagId": 33,
        "key": "greedy"
      },
      {
        "bojTagId": 124,
        "key": "math"
      }
    ],
    "lastupdate": 1687116861.575557
  },
  "2374": {
    "problemId": "2374",
    "problemLevel": 12,
    "problemName": "같은 수로 만들기",
    "average_try": 2.7872,
    "solvedtags": [
      {
        "bojTagId": 175,
        "key": "data_structures"
      },
      {
        "bojTagId": 33,
        "key": "greedy"
      },
      {
        "bojTagId": 71,
        "key": "stack"
      }
    ],
    "lastupdate": 1687116861.575575
  },
  "14600": {
    "problemId": "14600",
    "problemLevel": 10,
    "problemName": "샤워실 바닥 깔기 (Small)",
    "average_try": 1.4964,
    "solvedtags": [
      {
        "bojTagId": 24,
        "key": "divide_and_conquer"
      },
      {
        "bojTagId": 102,
        "key": "implementation"
      }
    ],
    "lastupdate": 1687116861.575625
  },
  "1030": {
    "problemId": "1030",
    "problemLevel": 13,
    "problemName": "프렉탈 평면",
    "average_try": 2.2067,
    "solvedtags": [
      {
        "bojTagId": 24,
        "key": "divide_and_conquer"
      },
      {
        "bojTagId": 102,
        "key": "implementation"
      },
      {
        "bojTagId": 62,
        "key": "recursion"
      }
    ],
    "lastupdate": 1687116861.575643
  },
  "16438": {
    "problemId": "16438",
    "problemLevel": 13,
    "problemName": "원숭이 스포츠",
    "average_try": 2.0431,
    "solvedtags": [
      {
        "bojTagId": 14,
        "key": "bitmask"
      },
      {
        "bojTagId": 128,
        "key": "constructive"
      },
      {
        "bojTagId": 24,
        "key": "divide_and_conquer"
      }
    ],
    "lastupdate": 1687116861.575661
  },
  "14601": {
    "problemId": "14601",
    "problemLevel": 16,
    "problemName": "샤워실 바닥 깔기 (Large)",
    "average_try": 1.7922,
    "solvedtags": [
      {
        "bojTagId": 24,
        "key": "divide_and_conquer"
      },
      {
        "bojTagId": 102,
        "key": "implementation"
      },
      {
        "bojTagId": 62,
        "key": "recursion"
      }
    ],
    "lastupdate": 1687116861.575679
  },
  "2448": {
    "problemId": "2448",
    "problemLevel": 12,
    "problemName": "별 찍기 - 11",
    "average_try": 2.4276,
    "solvedtags": [
      {
        "bojTagId": 62,
        "key": "recursion"
      }
    ],
    "lastupdate": 1687116861.575697
  },
  "10870": {
    "problemId": "10870",
    "problemLevel": 4,
    "problemName": "피보나치 수 5",
    "average_try": 1.6296,
    "solvedtags": [
      {
        "bojTagId": 102,
        "key": "implementation"
      },
      {
        "bojTagId": 124,
        "key": "math"
      }
    ],
    "lastupdate": 1687116861.576039
  },
  "2839": {
    "problemId": "2839",
    "problemLevel": 7,
    "problemName": "설탕 배달",
    "average_try": 2.7473,
    "solvedtags": [
      {
        "bojTagId": 25,
        "key": "dp"
      },
      {
        "bojTagId": 33,
        "key": "greedy"
      },
      {
        "bojTagId": 124,
        "key": "math"
      }
    ],
    "lastupdate": 1687116861.576071
  },
  "2748": {
    "problemId": "2748",
    "problemLevel": 5,
    "problemName": "피보나치 수 2",
    "average_try": 2.467,
    "solvedtags": [
      {
        "bojTagId": 25,
        "key": "dp"
      },
      {
        "bojTagId": 124,
        "key": "math"
      }
    ],
    "lastupdate": 1687116861.576091
  },
  "1010": {
    "problemId": "1010",
    "problemLevel": 6,
    "problemName": "다리 놓기",
    "average_try": 2.0678,
    "solvedtags": [
      {
        "bojTagId": 6,
        "key": "combinatorics"
      },
      {
        "bojTagId": 25,
        "key": "dp"
      },
      {
        "bojTagId": 124,
        "key": "math"
      }
    ],
    "lastupdate": 1687116861.57611
  },
  "9655": {
    "problemId": "9655",
    "problemLevel": 6,
    "problemName": "돌 게임",
    "average_try": 1.4856,
    "solvedtags": [
      {
        "bojTagId": 25,
        "key": "dp"
      },
      {
        "bojTagId": 140,
        "key": "game_theory"
      },
      {
        "bojTagId": 124,
        "key": "math"
      }
    ],
    "lastupdate": 1687116861.576128
  },
  "17626": {
    "problemId": "17626",
    "problemLevel": 8,
    "problemName": "Four Squares",
    "average_try": 2.2791,
    "solvedtags": [
      {
        "bojTagId": 125,
        "key": "bruteforcing"
      },
      {
        "bojTagId": 25,
        "key": "dp"
      }
    ],
    "lastupdate": 1687116861.576147
  },
  "15489": {
    "problemId": "15489",
    "problemLevel": 7,
    "problemName": "파스칼 삼각형",
    "average_try": 1.6596,
    "solvedtags": [
      {
        "bojTagId": 6,
        "key": "combinatorics"
      },
      {
        "bojTagId": 25,
        "key": "dp"
      },
      {
        "bojTagId": 124,
        "key": "math"
      }
    ],
    "lastupdate": 1687116861.576166
  },
  "14501": {
    "problemId": "14501",
    "problemLevel": 8,
    "problemName": "퇴사",
    "average_try": 2.0142,
    "solvedtags": [
      {
        "bojTagId": 125,
        "key": "bruteforcing"
      },
      {
        "bojTagId": 25,
        "key": "dp"
      }
    ],
    "lastupdate": 1687116861.576183
  },
  "2670": {
    "problemId": "2670",
    "problemLevel": 7,
    "problemName": "연속부분최대곱",
    "average_try": 2.8045,
    "solvedtags": [
      {
        "bojTagId": 125,
        "key": "bruteforcing"
      },
      {
        "bojTagId": 25,
        "key": "dp"
      }
    ],
    "lastupdate": 1687116861.576202
  },
  "13699": {
    "problemId": "13699",
    "problemLevel": 7,
    "problemName": "점화식",
    "average_try": 1.3543,
    "solvedtags": [
      {
        "bojTagId": 25,
        "key": "dp"
      }
    ],
    "lastupdate": 1687116861.57622
  },
  "1463": {
    "problemId": "1463",
    "problemLevel": 8,
    "problemName": "1로 만들기",
    "average_try": 3.0682,
    "solvedtags": [
      {
        "bojTagId": 25,
        "key": "dp"
      }
    ],
    "lastupdate": 1687116861.576238
  },
  "9095": {
    "problemId": "9095",
    "problemLevel": 8,
    "problemName": "1, 2, 3 더하기",
    "average_try": 1.5584,
    "solvedtags": [
      {
        "bojTagId": 25,
        "key": "dp"
      }
    ],
    "lastupdate": 1687116861.576256
  },
  "1003": {
    "problemId": "1003",
    "problemLevel": 8,
    "problemName": "피보나치 함수",
    "average_try": 3.0841,
    "solvedtags": [
      {
        "bojTagId": 25,
        "key": "dp"
      }
    ],
    "lastupdate": 1687116861.576274
  },
  "11726": {
    "problemId": "11726",
    "problemLevel": 8,
    "problemName": "2×n 타일링",
    "average_try": 2.7533,
    "solvedtags": [
      {
        "bojTagId": 25,
        "key": "dp"
      }
    ],
    "lastupdate": 1687116861.576293
  },
  "2579": {
    "problemId": "2579",
    "problemLevel": 8,
    "problemName": "계단 오르기",
    "average_try": 2.969,
    "solvedtags": [
      {
        "bojTagId": 25,
        "key": "dp"
      }
    ],
    "lastupdate": 1687116861.57631
  },
  "2193": {
    "problemId": "2193",
    "problemLevel": 8,
    "problemName": "이친수",
    "average_try": 2.4559,
    "solvedtags": [
      {
        "bojTagId": 25,
        "key": "dp"
      }
    ],
    "lastupdate": 1687116861.576329
  },
  "11727": {
    "problemId": "11727",
    "problemLevel": 8,
    "problemName": "2×n 타일링 2",
    "average_try": 1.6934,
    "solvedtags": [
      {
        "bojTagId": 25,
        "key": "dp"
      }
    ],
    "lastupdate": 1687116861.576346
  },
  "9461": {
    "problemId": "9461",
    "problemLevel": 8,
    "problemName": "파도반 수열",
    "average_try": 2.3301,
    "solvedtags": [
      {
        "bojTagId": 25,
        "key": "dp"
      },
      {
        "bojTagId": 124,
        "key": "math"
      }
    ],
    "lastupdate": 1687116861.576365
  },
  "1699": {
    "problemId": "1699",
    "problemLevel": 9,
    "problemName": "제곱수의 합",
    "average_try": 2.5362,
    "solvedtags": [
      {
        "bojTagId": 25,
        "key": "dp"
      },
      {
        "bojTagId": 124,
        "key": "math"
      }
    ],
    "lastupdate": 1687116861.576383
  },
  "15990": {
    "problemId": "15990",
    "problemLevel": 9,
    "problemName": "1, 2, 3 더하기 5",
    "average_try": 3.2298,
    "solvedtags": [
      {
        "bojTagId": 25,
        "key": "dp"
      }
    ],
    "lastupdate": 1687116861.5764
  },
  "10211": {
    "problemId": "10211",
    "problemLevel": 7,
    "problemName": "Maximum Subarray",
    "average_try": 2.3655,
    "solvedtags": [
      {
        "bojTagId": 125,
        "key": "bruteforcing"
      },
      {
        "bojTagId": 25,
        "key": "dp"
      },
      {
        "bojTagId": 139,
        "key": "prefix_sum"
      }
    ],
    "lastupdate": 1687116861.576417
  },
  "17175": {
    "problemId": "17175",
    "problemLevel": 8,
    "problemName": "피보나치는 지겨웡~",
    "average_try": 2.3579,
    "solvedtags": [
      {
        "bojTagId": 25,
        "key": "dp"
      }
    ],
    "lastupdate": 1687116861.576435
  },
  "15624": {
    "problemId": "15624",
    "problemLevel": 7,
    "problemName": "피보나치 수 7",
    "average_try": 1.9368,
    "solvedtags": [
      {
        "bojTagId": 25,
        "key": "dp"
      },
      {
        "bojTagId": 124,
        "key": "math"
      }
    ],
    "lastupdate": 1687116861.576452
  },
  "17212": {
    "problemId": "17212",
    "problemLevel": 8,
    "problemName": "달나라 토끼를 위한 구매대금 지불 도우미",
    "average_try": 2.0403,
    "solvedtags": [
      {
        "bojTagId": 25,
        "key": "dp"
      }
    ],
    "lastupdate": 1687116861.576469
  },
  "2876": {
    "problemId": "2876",
    "problemLevel": 9,
    "problemName": "그래픽스 퀴즈",
    "average_try": 2.1089,
    "solvedtags": [
      {
        "bojTagId": 25,
        "key": "dp"
      }
    ],
    "lastupdate": 1687116861.576487
  },
  "20152": {
    "problemId": "20152",
    "problemLevel": 9,
    "problemName": "Game Addiction",
    "average_try": 2.1238,
    "solvedtags": [
      {
        "bojTagId": 6,
        "key": "combinatorics"
      },
      {
        "bojTagId": 25,
        "key": "dp"
      },
      {
        "bojTagId": 124,
        "key": "math"
      }
    ],
    "lastupdate": 1687116861.576504
  },
  "11053": {
    "problemId": "11053",
    "problemLevel": 9,
    "problemName": "가장 긴 증가하는 부분 수열",
    "average_try": 2.6564,
    "solvedtags": [
      {
        "bojTagId": 25,
        "key": "dp"
      }
    ],
    "lastupdate": 1687116861.576522
  },
  "1912": {
    "problemId": "1912",
    "problemLevel": 9,
    "problemName": "연속합",
    "average_try": 2.8198,
    "solvedtags": [
      {
        "bojTagId": 25,
        "key": "dp"
      }
    ],
    "lastupdate": 1687116861.576539
  },
  "9465": {
    "problemId": "9465",
    "problemLevel": 10,
    "problemName": "스티커",
    "average_try": 2.1407,
    "solvedtags": [
      {
        "bojTagId": 25,
        "key": "dp"
      }
    ],
    "lastupdate": 1687116861.576557
  },
  "11055": {
    "problemId": "11055",
    "problemLevel": 9,
    "problemName": "가장 큰 증가하는 부분 수열",
    "average_try": 2.238,
    "solvedtags": [
      {
        "bojTagId": 25,
        "key": "dp"
      }
    ],
    "lastupdate": 1687116861.576575
  },
  "11722": {
    "problemId": "11722",
    "problemLevel": 9,
    "problemName": "가장 긴 감소하는 부분 수열",
    "average_try": 1.5702,
    "solvedtags": [
      {
        "bojTagId": 25,
        "key": "dp"
      }
    ],
    "lastupdate": 1687116861.576592
  },
  "1890": {
    "problemId": "1890",
    "problemLevel": 10,
    "problemName": "점프",
    "average_try": 3.3221,
    "solvedtags": [
      {
        "bojTagId": 25,
        "key": "dp"
      }
    ],
    "lastupdate": 1687116861.57661
  },
  "1965": {
    "problemId": "1965",
    "problemLevel": 9,
    "problemName": "상자넣기",
    "average_try": 2.0241,
    "solvedtags": [
      {
        "bojTagId": 25,
        "key": "dp"
      }
    ],
    "lastupdate": 1687116861.576627
  },
  "2407": {
    "problemId": "2407",
    "problemLevel": 8,
    "problemName": "조합",
    "average_try": 2.3749,
    "solvedtags": [
      {
        "bojTagId": 117,
        "key": "arbitrary_precision"
      },
      {
        "bojTagId": 6,
        "key": "combinatorics"
      },
      {
        "bojTagId": 124,
        "key": "math"
      }
    ],
    "lastupdate": 1687116861.576645
  },
  "11060": {
    "problemId": "11060",
    "problemLevel": 9,
    "problemName": "점프 점프",
    "average_try": 2.7852,
    "solvedtags": [
      {
        "bojTagId": 126,
        "key": "bfs"
      },
      {
        "bojTagId": 25,
        "key": "dp"
      },
      {
        "bojTagId": 7,
        "key": "graphs"
      },
      {
        "bojTagId": 11,
        "key": "graph_traversal"
      }
    ],
    "lastupdate": 1687116861.576662
  },
  "15988": {
    "problemId": "15988",
    "problemLevel": 9,
    "problemName": "1, 2, 3 더하기 3",
    "average_try": 2.8699,
    "solvedtags": [
      {
        "bojTagId": 25,
        "key": "dp"
      }
    ],
    "lastupdate": 1687116861.576679
  },
  "2491": {
    "problemId": "2491",
    "problemLevel": 7,
    "problemName": "수열",
    "average_try": 2.9715,
    "solvedtags": [
      {
        "bojTagId": 25,
        "key": "dp"
      },
      {
        "bojTagId": 102,
        "key": "implementation"
      }
    ],
    "lastupdate": 1687116861.576697
  },
  "15486": {
    "problemId": "15486",
    "problemLevel": 11,
    "problemName": "퇴사 2",
    "average_try": 2.5976,
    "solvedtags": [
      {
        "bojTagId": 25,
        "key": "dp"
      }
    ],
    "lastupdate": 1687116861.576714
  },
  "1660": {
    "problemId": "1660",
    "problemLevel": 10,
    "problemName": "캡틴 이다솜",
    "average_try": 2.9563,
    "solvedtags": [
      {
        "bojTagId": 25,
        "key": "dp"
      }
    ],
    "lastupdate": 1687116861.576732
  },
  "14852": {
    "problemId": "14852",
    "problemLevel": 12,
    "problemName": "타일 채우기 3",
    "average_try": 3.9275,
    "solvedtags": [
      {
        "bojTagId": 25,
        "key": "dp"
      }
    ],
    "lastupdate": 1687116861.576749
  },
  "14430": {
    "problemId": "14430",
    "problemLevel": 9,
    "problemName": "자원 캐기",
    "average_try": 1.8039,
    "solvedtags": [
      {
        "bojTagId": 25,
        "key": "dp"
      }
    ],
    "lastupdate": 1687116861.576767
  },
  "1633": {
    "problemId": "1633",
    "problemLevel": 12,
    "problemName": "최고의 팀 만들기",
    "average_try": 2.3307,
    "solvedtags": [
      {
        "bojTagId": 25,
        "key": "dp"
      }
    ],
    "lastupdate": 1687116861.576784
  },
  "18353": {
    "problemId": "18353",
    "problemLevel": 9,
    "problemName": "병사 배치하기",
    "average_try": 2.4415,
    "solvedtags": [
      {
        "bojTagId": 25,
        "key": "dp"
      },
      {
        "bojTagId": 43,
        "key": "lis"
      }
    ],
    "lastupdate": 1687116861.576801
  },
  "1106": {
    "problemId": "1106",
    "problemLevel": 11,
    "problemName": "호텔",
    "average_try": 2.8938,
    "solvedtags": [
      {
        "bojTagId": 25,
        "key": "dp"
      },
      {
        "bojTagId": 148,
        "key": "knapsack"
      }
    ],
    "lastupdate": 1687116861.576818
  },
  "17291": {
    "problemId": "17291",
    "problemLevel": 9,
    "problemName": "새끼치기",
    "average_try": 2.4101,
    "solvedtags": [
      {
        "bojTagId": 25,
        "key": "dp"
      },
      {
        "bojTagId": 102,
        "key": "implementation"
      }
    ],
    "lastupdate": 1687116861.576836
  },
  "4097": {
    "problemId": "4097",
    "problemLevel": 9,
    "problemName": "수익",
    "average_try": 2.1586,
    "solvedtags": [
      {
        "bojTagId": 25,
        "key": "dp"
      }
    ],
    "lastupdate": 1687116861.576853
  },
  "20162": {
    "problemId": "20162",
    "problemLevel": 9,
    "problemName": "간식 파티",
    "average_try": 1.8339,
    "solvedtags": [
      {
        "bojTagId": 25,
        "key": "dp"
      }
    ],
    "lastupdate": 1687116861.57687
  },
  "1149": {
    "problemId": "1149",
    "problemLevel": 10,
    "problemName": "RGB거리",
    "average_try": 1.8616,
    "solvedtags": [
      {
        "bojTagId": 25,
        "key": "dp"
      }
    ],
    "lastupdate": 1687116861.576887
  },
  "1932": {
    "problemId": "1932",
    "problemLevel": 10,
    "problemName": "정수 삼각형",
    "average_try": 1.6916,
    "solvedtags": [
      {
        "bojTagId": 25,
        "key": "dp"
      }
    ],
    "lastupdate": 1687116861.576905
  },
  "2156": {
    "problemId": "2156",
    "problemLevel": 10,
    "problemName": "포도주 시식",
    "average_try": 3.0714,
    "solvedtags": [
      {
        "bojTagId": 25,
        "key": "dp"
      }
    ],
    "lastupdate": 1687116861.576922
  },
  "10844": {
    "problemId": "10844",
    "problemLevel": 10,
    "problemName": "쉬운 계단 수",
    "average_try": 3.3129,
    "solvedtags": [
      {
        "bojTagId": 25,
        "key": "dp"
      }
    ],
    "lastupdate": 1687116861.576939
  },
  "11052": {
    "problemId": "11052",
    "problemLevel": 10,
    "problemName": "카드 구매하기",
    "average_try": 1.6345,
    "solvedtags": [
      {
        "bojTagId": 25,
        "key": "dp"
      }
    ],
    "lastupdate": 1687116861.576956
  },
  "11057": {
    "problemId": "11057",
    "problemLevel": 10,
    "problemName": "오르막 수",
    "average_try": 2.0945,
    "solvedtags": [
      {
        "bojTagId": 25,
        "key": "dp"
      }
    ],
    "lastupdate": 1687116861.576973
  },
  "2293": {
    "problemId": "2293",
    "problemLevel": 11,
    "problemName": "동전 1",
    "average_try": 2.1698,
    "solvedtags": [
      {
        "bojTagId": 25,
        "key": "dp"
      }
    ],
    "lastupdate": 1687116861.57699
  },
  "11051": {
    "problemId": "11051",
    "problemLevel": 9,
    "problemName": "이항 계수 2",
    "average_try": 2.6579,
    "solvedtags": [
      {
        "bojTagId": 6,
        "key": "combinatorics"
      },
      {
        "bojTagId": 25,
        "key": "dp"
      },
      {
        "bojTagId": 124,
        "key": "math"
      }
    ],
    "lastupdate": 1687116861.577008
  },
  "11048": {
    "problemId": "11048",
    "problemLevel": 9,
    "problemName": "이동하기",
    "average_try": 1.7132,
    "solvedtags": [
      {
        "bojTagId": 25,
        "key": "dp"
      }
    ],
    "lastupdate": 1687116861.577025
  },
  "2294": {
    "problemId": "2294",
    "problemLevel": 11,
    "problemName": "동전 2",
    "average_try": 3.4072,
    "solvedtags": [
      {
        "bojTagId": 25,
        "key": "dp"
      }
    ],
    "lastupdate": 1687116861.577042
  },
  "1309": {
    "problemId": "1309",
    "problemLevel": 10,
    "problemName": "동물원",
    "average_try": 2.114,
    "solvedtags": [
      {
        "bojTagId": 25,
        "key": "dp"
      }
    ],
    "lastupdate": 1687116861.577059
  },
  "2565": {
    "problemId": "2565",
    "problemLevel": 11,
    "problemName": "전깃줄",
    "average_try": 2.1295,
    "solvedtags": [
      {
        "bojTagId": 25,
        "key": "dp"
      }
    ],
    "lastupdate": 1687116861.577076
  },
  "2011": {
    "problemId": "2011",
    "problemLevel": 11,
    "problemName": "암호코드",
    "average_try": 5.0086,
    "solvedtags": [
      {
        "bojTagId": 25,
        "key": "dp"
      }
    ],
    "lastupdate": 1687116861.577093
  },
  "10164": {
    "problemId": "10164",
    "problemLevel": 10,
    "problemName": "격자상의 경로",
    "average_try": 2.7864,
    "solvedtags": [
      {
        "bojTagId": 6,
        "key": "combinatorics"
      },
      {
        "bojTagId": 25,
        "key": "dp"
      },
      {
        "bojTagId": 124,
        "key": "math"
      }
    ],
    "lastupdate": 1687116861.577128
  },
  "16194": {
    "problemId": "16194",
    "problemLevel": 10,
    "problemName": "카드 구매하기 2",
    "average_try": 1.3148,
    "solvedtags": [
      {
        "bojTagId": 25,
        "key": "dp"
      }
    ],
    "lastupdate": 1687116861.577146
  },
  "19622": {
    "problemId": "19622",
    "problemLevel": 9,
    "problemName": "회의실 배정 3",
    "average_try": 2.1745,
    "solvedtags": [
      {
        "bojTagId": 25,
        "key": "dp"
      }
    ],
    "lastupdate": 1687116861.577163
  },
  "15989": {
    "problemId": "15989",
    "problemLevel": 10,
    "problemName": "1, 2, 3 더하기 4",
    "average_try": 1.5424,
    "solvedtags": [
      {
        "bojTagId": 25,
        "key": "dp"
      }
    ],
    "lastupdate": 1687116861.57718
  },
  "12101": {
    "problemId": "12101",
    "problemLevel": 10,
    "problemName": "1, 2, 3 더하기 2",
    "average_try": 1.6004,
    "solvedtags": [
      {
        "bojTagId": 5,
        "key": "backtracking"
      },
      {
        "bojTagId": 125,
        "key": "bruteforcing"
      }
    ],
    "lastupdate": 1687116861.577197
  },
  "15992": {
    "problemId": "15992",
    "problemLevel": 10,
    "problemName": "1, 2, 3 더하기 7",
    "average_try": 1.9391,
    "solvedtags": [
      {
        "bojTagId": 25,
        "key": "dp"
      }
    ],
    "lastupdate": 1687116861.577215
  },
  "15991": {
    "problemId": "15991",
    "problemLevel": 10,
    "problemName": "1, 2, 3 더하기 6",
    "average_try": 2.0944,
    "solvedtags": [
      {
        "bojTagId": 25,
        "key": "dp"
      }
    ],
    "lastupdate": 1687116861.577232
  },
  "16195": {
    "problemId": "16195",
    "problemLevel": 10,
    "problemName": "1, 2, 3 더하기 9",
    "average_try": 1.8529,
    "solvedtags": [
      {
        "bojTagId": 25,
        "key": "dp"
      }
    ],
    "lastupdate": 1687116861.577249
  },
  "15993": {
    "problemId": "15993",
    "problemLevel": 10,
    "problemName": "1, 2, 3 더하기 8",
    "average_try": 1.7546,
    "solvedtags": [
      {
        "bojTagId": 25,
        "key": "dp"
      }
    ],
    "lastupdate": 1687116861.577266
  },
  "1495": {
    "problemId": "1495",
    "problemLevel": 10,
    "problemName": "기타리스트",
    "average_try": 2.7097,
    "solvedtags": [
      {
        "bojTagId": 25,
        "key": "dp"
      }
    ],
    "lastupdate": 1687116861.577283
  },
  "2302": {
    "problemId": "2302",
    "problemLevel": 10,
    "problemName": "극장 좌석",
    "average_try": 2.4772,
    "solvedtags": [
      {
        "bojTagId": 25,
        "key": "dp"
      }
    ],
    "lastupdate": 1687116861.5773
  },
  "11568": {
    "problemId": "11568",
    "problemLevel": 9,
    "problemName": "민균이의 계략",
    "average_try": 1.8312,
    "solvedtags": [
      {
        "bojTagId": 25,
        "key": "dp"
      },
      {
        "bojTagId": 43,
        "key": "lis"
      }
    ],
    "lastupdate": 1687116861.577317
  },
  "12026": {
    "problemId": "12026",
    "problemLevel": 10,
    "problemName": "BOJ 거리",
    "average_try": 1.6361,
    "solvedtags": [
      {
        "bojTagId": 25,
        "key": "dp"
      }
    ],
    "lastupdate": 1687116861.577334
  },
  "14722": {
    "problemId": "14722",
    "problemLevel": 12,
    "problemName": "우유 도시",
    "average_try": 3.2495,
    "solvedtags": [
      {
        "bojTagId": 25,
        "key": "dp"
      }
    ],
    "lastupdate": 1687116861.577352
  },
  "13910": {
    "problemId": "13910",
    "problemLevel": 11,
    "problemName": "개업",
    "average_try": 3.2043,
    "solvedtags": [
      {
        "bojTagId": 25,
        "key": "dp"
      }
    ],
    "lastupdate": 1687116861.577369
  },
  "21317": {
    "problemId": "21317",
    "problemLevel": 10,
    "problemName": "징검다리 건너기",
    "average_try": 3.5706,
    "solvedtags": [
      {
        "bojTagId": 25,
        "key": "dp"
      }
    ],
    "lastupdate": 1687116861.577387
  },
  "22857": {
    "problemId": "22857",
    "problemLevel": 9,
    "problemName": "가장 긴 짝수 연속한 부분 수열 (small)",
    "average_try": 2.5575,
    "solvedtags": [
      {
        "bojTagId": 25,
        "key": "dp"
      },
      {
        "bojTagId": 80,
        "key": "two_pointer"
      }
    ],
    "lastupdate": 1687116861.577405
  },
  "22869": {
    "problemId": "22869",
    "problemLevel": 10,
    "problemName": "징검다리 건너기 (small)",
    "average_try": 2.5889,
    "solvedtags": [
      {
        "bojTagId": 25,
        "key": "dp"
      }
    ],
    "lastupdate": 1687116861.577422
  },
  "22871": {
    "problemId": "22871",
    "problemLevel": 10,
    "problemName": "징검다리 건너기 (large)",
    "average_try": 3.3179,
    "solvedtags": [
      {
        "bojTagId": 12,
        "key": "binary_search"
      },
      {
        "bojTagId": 25,
        "key": "dp"
      }
    ],
    "lastupdate": 1687116861.577439
  },
  "1535": {
    "problemId": "1535",
    "problemLevel": 9,
    "problemName": "안녕",
    "average_try": 1.8562,
    "solvedtags": [
      {
        "bojTagId": 125,
        "key": "bruteforcing"
      },
      {
        "bojTagId": 25,
        "key": "dp"
      },
      {
        "bojTagId": 148,
        "key": "knapsack"
      }
    ],
    "lastupdate": 1687116861.578306
  },
  "9084": {
    "problemId": "9084",
    "problemLevel": 11,
    "problemName": "동전",
    "average_try": 1.5077,
    "solvedtags": [
      {
        "bojTagId": 25,
        "key": "dp"
      },
      {
        "bojTagId": 148,
        "key": "knapsack"
      }
    ],
    "lastupdate": 1687116861.578332
  },
  "3067": {
    "problemId": "3067",
    "problemLevel": 11,
    "problemName": "Coins",
    "average_try": 1.2906,
    "solvedtags": [
      {
        "bojTagId": 25,
        "key": "dp"
      },
      {
        "bojTagId": 148,
        "key": "knapsack"
      }
    ],
    "lastupdate": 1687116861.578352
  },
  "12865": {
    "problemId": "12865",
    "problemLevel": 11,
    "problemName": "평범한 배낭",
    "average_try": 2.8135,
    "solvedtags": [
      {
        "bojTagId": 25,
        "key": "dp"
      },
      {
        "bojTagId": 148,
        "key": "knapsack"
      }
    ],
    "lastupdate": 1687116861.578371
  },
  "14728": {
    "problemId": "14728",
    "problemLevel": 11,
    "problemName": "벼락치기",
    "average_try": 1.9577,
    "solvedtags": [
      {
        "bojTagId": 25,
        "key": "dp"
      },
      {
        "bojTagId": 148,
        "key": "knapsack"
      }
    ],
    "lastupdate": 1687116861.578389
  },
  "17845": {
    "problemId": "17845",
    "problemLevel": 11,
    "problemName": "수강 과목",
    "average_try": 1.7129,
    "solvedtags": [
      {
        "bojTagId": 25,
        "key": "dp"
      },
      {
        "bojTagId": 148,
        "key": "knapsack"
      }
    ],
    "lastupdate": 1687116861.578408
  },
  "17208": {
    "problemId": "17208",
    "problemLevel": 12,
    "problemName": "카우버거 알바생",
    "average_try": 2.3352,
    "solvedtags": [
      {
        "bojTagId": 25,
        "key": "dp"
      },
      {
        "bojTagId": 148,
        "key": "knapsack"
      }
    ],
    "lastupdate": 1687116861.578426
  },
  "18427": {
    "problemId": "18427",
    "problemLevel": 12,
    "problemName": "함께 블록 쌓기",
    "average_try": 2.4816,
    "solvedtags": [
      {
        "bojTagId": 25,
        "key": "dp"
      },
      {
        "bojTagId": 148,
        "key": "knapsack"
      }
    ],
    "lastupdate": 1687116861.578443
  },
  "7579": {
    "problemId": "7579",
    "problemLevel": 13,
    "problemName": "앱",
    "average_try": 2.7008,
    "solvedtags": [
      {
        "bojTagId": 25,
        "key": "dp"
      },
      {
        "bojTagId": 148,
        "key": "knapsack"
      }
    ],
    "lastupdate": 1687116861.578462
  },
  "2629": {
    "problemId": "2629",
    "problemLevel": 13,
    "problemName": "양팔저울",
    "average_try": 3.0804,
    "solvedtags": [
      {
        "bojTagId": 25,
        "key": "dp"
      },
      {
        "bojTagId": 148,
        "key": "knapsack"
      }
    ],
    "lastupdate": 1687116861.578481
  },
  "19645": {
    "problemId": "19645",
    "problemLevel": 15,
    "problemName": "햄최몇?",
    "average_try": 2.6513,
    "solvedtags": [
      {
        "bojTagId": 25,
        "key": "dp"
      },
      {
        "bojTagId": 148,
        "key": "knapsack"
      }
    ],
    "lastupdate": 1687116861.5785
  },
  "20667": {
    "problemId": "20667",
    "problemLevel": 15,
    "problemName": "크롬",
    "average_try": 5.3388,
    "solvedtags": [
      {
        "bojTagId": 25,
        "key": "dp"
      },
      {
        "bojTagId": 148,
        "key": "knapsack"
      }
    ],
    "lastupdate": 1687116861.578518
  },
  "9251": {
    "problemId": "9251",
    "problemLevel": 11,
    "problemName": "LCS",
    "average_try": 2.4836,
    "solvedtags": [
      {
        "bojTagId": 25,
        "key": "dp"
      },
      {
        "bojTagId": 158,
        "key": "string"
      }
    ],
    "lastupdate": 1687116861.578535
  },
  "2225": {
    "problemId": "2225",
    "problemLevel": 11,
    "problemName": "합분해",
    "average_try": 2.3167,
    "solvedtags": [
      {
        "bojTagId": 25,
        "key": "dp"
      },
      {
        "bojTagId": 124,
        "key": "math"
      }
    ],
    "lastupdate": 1687116861.578553
  },
  "1915": {
    "problemId": "1915",
    "problemLevel": 12,
    "problemName": "가장 큰 정사각형",
    "average_try": 3.408,
    "solvedtags": [
      {
        "bojTagId": 25,
        "key": "dp"
      }
    ],
    "lastupdate": 1687116861.578571
  },
  "17070": {
    "problemId": "17070",
    "problemLevel": 11,
    "problemName": "파이프 옮기기 1",
    "average_try": 2.1855,
    "solvedtags": [
      {
        "bojTagId": 25,
        "key": "dp"
      },
      {
        "bojTagId": 7,
        "key": "graphs"
      },
      {
        "bojTagId": 11,
        "key": "graph_traversal"
      }
    ],
    "lastupdate": 1687116861.578589
  },
  "5557": {
    "problemId": "5557",
    "problemLevel": 11,
    "problemName": "1학년",
    "average_try": 2.2645,
    "solvedtags": [
      {
        "bojTagId": 25,
        "key": "dp"
      }
    ],
    "lastupdate": 1687116861.578607
  },
  "2631": {
    "problemId": "2631",
    "problemLevel": 12,
    "problemName": "줄세우기",
    "average_try": 1.5371,
    "solvedtags": [
      {
        "bojTagId": 25,
        "key": "dp"
      }
    ],
    "lastupdate": 1687116861.578625
  },
  "14226": {
    "problemId": "14226",
    "problemLevel": 12,
    "problemName": "이모티콘",
    "average_try": 2.9399,
    "solvedtags": [
      {
        "bojTagId": 126,
        "key": "bfs"
      },
      {
        "bojTagId": 7,
        "key": "graphs"
      },
      {
        "bojTagId": 11,
        "key": "graph_traversal"
      }
    ],
    "lastupdate": 1687116861.578643
  },
  "5582": {
    "problemId": "5582",
    "problemLevel": 11,
    "problemName": "공통 부분 문자열",
    "average_try": 2.3726,
    "solvedtags": [
      {
        "bojTagId": 25,
        "key": "dp"
      },
      {
        "bojTagId": 158,
        "key": "string"
      }
    ],
    "lastupdate": 1687116861.57866
  },
  "13398": {
    "problemId": "13398",
    "problemLevel": 11,
    "problemName": "연속합 2",
    "average_try": 3.3717,
    "solvedtags": [
      {
        "bojTagId": 25,
        "key": "dp"
      }
    ],
    "lastupdate": 1687116861.578678
  },
  "4811": {
    "problemId": "4811",
    "problemLevel": 11,
    "problemName": "알약",
    "average_try": 1.4855,
    "solvedtags": [
      {
        "bojTagId": 25,
        "key": "dp"
      },
      {
        "bojTagId": 124,
        "key": "math"
      }
    ],
    "lastupdate": 1687116861.578695
  },
  "2688": {
    "problemId": "2688",
    "problemLevel": 10,
    "problemName": "줄어들지 않아",
    "average_try": 1.9144,
    "solvedtags": [
      {
        "bojTagId": 25,
        "key": "dp"
      }
    ],
    "lastupdate": 1687116861.578713
  },
  "2624": {
    "problemId": "2624",
    "problemLevel": 11,
    "problemName": "동전 바꿔주기",
    "average_try": 2.0461,
    "solvedtags": [
      {
        "bojTagId": 25,
        "key": "dp"
      }
    ],
    "lastupdate": 1687116861.57873
  },
  "13302": {
    "problemId": "13302",
    "problemLevel": 12,
    "problemName": "리조트",
    "average_try": 2.2555,
    "solvedtags": [
      {
        "bojTagId": 25,
        "key": "dp"
      }
    ],
    "lastupdate": 1687116861.578747
  },
  "2228": {
    "problemId": "2228",
    "problemLevel": 13,
    "problemName": "구간 나누기",
    "average_try": 3.3825,
    "solvedtags": [
      {
        "bojTagId": 25,
        "key": "dp"
      }
    ],
    "lastupdate": 1687116861.578765
  },
  "17069": {
    "problemId": "17069",
    "problemLevel": 12,
    "problemName": "파이프 옮기기 2",
    "average_try": 1.7186,
    "solvedtags": [
      {
        "bojTagId": 25,
        "key": "dp"
      }
    ],
    "lastupdate": 1687116861.578783
  },
  "2229": {
    "problemId": "2229",
    "problemLevel": 11,
    "problemName": "조 짜기",
    "average_try": 1.6337,
    "solvedtags": [
      {
        "bojTagId": 25,
        "key": "dp"
      }
    ],
    "lastupdate": 1687116861.5788
  },
  "5569": {
    "problemId": "5569",
    "problemLevel": 12,
    "problemName": "출근 경로",
    "average_try": 1.9523,
    "solvedtags": [
      {
        "bojTagId": 25,
        "key": "dp"
      }
    ],
    "lastupdate": 1687116861.578818
  },
  "5624": {
    "problemId": "5624",
    "problemLevel": 13,
    "problemName": "좋은 수",
    "average_try": 2.9485,
    "solvedtags": [
      {
        "bojTagId": 25,
        "key": "dp"
      }
    ],
    "lastupdate": 1687116861.578835
  },
  "14925": {
    "problemId": "14925",
    "problemLevel": 12,
    "problemName": "목장 건설하기",
    "average_try": 2.55,
    "solvedtags": [
      {
        "bojTagId": 25,
        "key": "dp"
      }
    ],
    "lastupdate": 1687116861.578854
  },
  "14699": {
    "problemId": "14699",
    "problemLevel": 11,
    "problemName": "관악산 등산",
    "average_try": 2.1869,
    "solvedtags": [
      {
        "bojTagId": 25,
        "key": "dp"
      },
      {
        "bojTagId": 7,
        "key": "graphs"
      }
    ],
    "lastupdate": 1687116861.578872
  },
  "17265": {
    "problemId": "17265",
    "problemLevel": 11,
    "problemName": "나의 인생에는 수학과 함께",
    "average_try": 1.9307,
    "solvedtags": [
      {
        "bojTagId": 125,
        "key": "bruteforcing"
      },
      {
        "bojTagId": 127,
        "key": "dfs"
      },
      {
        "bojTagId": 25,
        "key": "dp"
      },
      {
        "bojTagId": 7,
        "key": "graphs"
      },
      {
        "bojTagId": 11,
        "key": "graph_traversal"
      }
    ],
    "lastupdate": 1687116861.578908
  },
  "1757": {
    "problemId": "1757",
    "problemLevel": 12,
    "problemName": "달려달려",
    "average_try": 2.7092,
    "solvedtags": [
      {
        "bojTagId": 25,
        "key": "dp"
      }
    ],
    "lastupdate": 1687116861.578926
  },
  "4095": {
    "problemId": "4095",
    "problemLevel": 12,
    "problemName": "최대 정사각형",
    "average_try": 2.44,
    "solvedtags": [
      {
        "bojTagId": 25,
        "key": "dp"
      }
    ],
    "lastupdate": 1687116861.578943
  },
  "2758": {
    "problemId": "2758",
    "problemLevel": 12,
    "problemName": "로또",
    "average_try": 3.8851,
    "solvedtags": [
      {
        "bojTagId": 25,
        "key": "dp"
      }
    ],
    "lastupdate": 1687116861.578961
  },
  "10653": {
    "problemId": "10653",
    "problemLevel": 13,
    "problemName": "마라톤 2",
    "average_try": 2.6347,
    "solvedtags": [
      {
        "bojTagId": 25,
        "key": "dp"
      }
    ],
    "lastupdate": 1687116861.578978
  },
  "16400": {
    "problemId": "16400",
    "problemLevel": 11,
    "problemName": "소수 화폐",
    "average_try": 2.2381,
    "solvedtags": [
      {
        "bojTagId": 25,
        "key": "dp"
      },
      {
        "bojTagId": 124,
        "key": "math"
      },
      {
        "bojTagId": 95,
        "key": "number_theory"
      },
      {
        "bojTagId": 9,
        "key": "primality_test"
      },
      {
        "bojTagId": 67,
        "key": "sieve"
      }
    ],
    "lastupdate": 1687116861.578996
  },
  "17216": {
    "problemId": "17216",
    "problemLevel": 10,
    "problemName": "가장 큰 감소 부분 수열",
    "average_try": 1.7056,
    "solvedtags": [
      {
        "bojTagId": 25,
        "key": "dp"
      }
    ],
    "lastupdate": 1687116861.579013
  },
  "11985": {
    "problemId": "11985",
    "problemLevel": 12,
    "problemName": "오렌지 출하",
    "average_try": 2.1763,
    "solvedtags": [
      {
        "bojTagId": 25,
        "key": "dp"
      }
    ],
    "lastupdate": 1687116861.579031
  },
  "17485": {
    "problemId": "17485",
    "problemLevel": 11,
    "problemName": "진우의 달 여행 (Large)",
    "average_try": 2.0872,
    "solvedtags": [
      {
        "bojTagId": 25,
        "key": "dp"
      }
    ],
    "lastupdate": 1687116861.579048
  },
  "15724": {
    "problemId": "15724",
    "problemLevel": 10,
    "problemName": "주지수",
    "average_try": 2.3621,
    "solvedtags": [
      {
        "bojTagId": 25,
        "key": "dp"
      },
      {
        "bojTagId": 139,
        "key": "prefix_sum"
      }
    ],
    "lastupdate": 1687116861.579067
  },
  "17255": {
    "problemId": "17255",
    "problemLevel": 12,
    "problemName": "N으로 만들기",
    "average_try": 2.0272,
    "solvedtags": [
      {
        "bojTagId": 5,
        "key": "backtracking"
      },
      {
        "bojTagId": 175,
        "key": "data_structures"
      },
      {
        "bojTagId": 74,
        "key": "tree_set"
      }
    ],
    "lastupdate": 1687116861.579102
  },
  "2073": {
    "problemId": "2073",
    "problemLevel": 12,
    "problemName": "수도배관공사",
    "average_try": 2.7323,
    "solvedtags": [
      {
        "bojTagId": 25,
        "key": "dp"
      },
      {
        "bojTagId": 148,
        "key": "knapsack"
      }
    ],
    "lastupdate": 1687116861.579119
  },
  "1520": {
    "problemId": "1520",
    "problemLevel": 13,
    "problemName": "내리막 길",
    "average_try": 3.5732,
    "solvedtags": [
      {
        "bojTagId": 127,
        "key": "dfs"
      },
      {
        "bojTagId": 25,
        "key": "dp"
      },
      {
        "bojTagId": 7,
        "key": "graphs"
      },
      {
        "bojTagId": 11,
        "key": "graph_traversal"
      }
    ],
    "lastupdate": 1687116861.579137
  },
  "2602": {
    "problemId": "2602",
    "problemLevel": 12,
    "problemName": "돌다리 건너기",
    "average_try": 2.0404,
    "solvedtags": [
      {
        "bojTagId": 25,
        "key": "dp"
      }
    ],
    "lastupdate": 1687116861.579173
  },
  "2616": {
    "problemId": "2616",
    "problemLevel": 13,
    "problemName": "소형기관차",
    "average_try": 2.2373,
    "solvedtags": [
      {
        "bojTagId": 25,
        "key": "dp"
      },
      {
        "bojTagId": 139,
        "key": "prefix_sum"
      }
    ],
    "lastupdate": 1687116861.57919
  },
  "17404": {
    "problemId": "17404",
    "problemLevel": 12,
    "problemName": "RGB거리 2",
    "average_try": 1.7204,
    "solvedtags": [
      {
        "bojTagId": 25,
        "key": "dp"
      }
    ],
    "lastupdate": 1687116861.579207
  },
  "1695": {
    "problemId": "1695",
    "problemLevel": 12,
    "problemName": "팰린드롬 만들기",
    "average_try": 2.7809,
    "solvedtags": [
      {
        "bojTagId": 25,
        "key": "dp"
      }
    ],
    "lastupdate": 1687116861.579225
  },
  "2157": {
    "problemId": "2157",
    "problemLevel": 12,
    "problemName": "여행",
    "average_try": 4.7895,
    "solvedtags": [
      {
        "bojTagId": 25,
        "key": "dp"
      },
      {
        "bojTagId": 7,
        "key": "graphs"
      }
    ],
    "lastupdate": 1687116861.579243
  },
  "14863": {
    "problemId": "14863",
    "problemLevel": 12,
    "problemName": "서울에서 경산까지",
    "average_try": 3.3207,
    "solvedtags": [
      {
        "bojTagId": 25,
        "key": "dp"
      }
    ],
    "lastupdate": 1687116861.57926
  },
  "1577": {
    "problemId": "1577",
    "problemLevel": 11,
    "problemName": "도로의 개수",
    "average_try": 3.3097,
    "solvedtags": [
      {
        "bojTagId": 25,
        "key": "dp"
      }
    ],
    "lastupdate": 1687116861.579278
  },
  "2411": {
    "problemId": "2411",
    "problemLevel": 12,
    "problemName": "아이템 먹기",
    "average_try": 2.4469,
    "solvedtags": [
      {
        "bojTagId": 25,
        "key": "dp"
      }
    ],
    "lastupdate": 1687116861.579314
  },
  "1301": {
    "problemId": "1301",
    "problemLevel": 13,
    "problemName": "비즈 공예",
    "average_try": 3.2776,
    "solvedtags": [
      {
        "bojTagId": 25,
        "key": "dp"
      }
    ],
    "lastupdate": 1687116861.579332
  },
  "2253": {
    "problemId": "2253",
    "problemLevel": 12,
    "problemName": "점프",
    "average_try": 3.9542,
    "solvedtags": [
      {
        "bojTagId": 25,
        "key": "dp"
      }
    ],
    "lastupdate": 1687116861.57935
  },
  "13902": {
    "problemId": "13902",
    "problemLevel": 12,
    "problemName": "개업 2",
    "average_try": 4.1696,
    "solvedtags": [
      {
        "bojTagId": 25,
        "key": "dp"
      }
    ],
    "lastupdate": 1687116861.579367
  },
  "13707": {
    "problemId": "13707",
    "problemLevel": 12,
    "problemName": "합분해 2",
    "average_try": 2.2287,
    "solvedtags": [
      {
        "bojTagId": 6,
        "key": "combinatorics"
      },
      {
        "bojTagId": 25,
        "key": "dp"
      },
      {
        "bojTagId": 124,
        "key": "math"
      }
    ],
    "lastupdate": 1687116861.579385
  },
  "14945": {
    "problemId": "14945",
    "problemLevel": 12,
    "problemName": "불장난",
    "average_try": 1.7811,
    "solvedtags": [
      {
        "bojTagId": 25,
        "key": "dp"
      }
    ],
    "lastupdate": 1687116861.579402
  },
  "1943": {
    "problemId": "1943",
    "problemLevel": 13,
    "problemName": "동전 분배",
    "average_try": 5.0104,
    "solvedtags": [
      {
        "bojTagId": 25,
        "key": "dp"
      },
      {
        "bojTagId": 148,
        "key": "knapsack"
      }
    ],
    "lastupdate": 1687116861.57942
  },
  "20542": {
    "problemId": "20542",
    "problemLevel": 13,
    "problemName": "받아쓰기",
    "average_try": 2.246,
    "solvedtags": [
      {
        "bojTagId": 25,
        "key": "dp"
      },
      {
        "bojTagId": 158,
        "key": "string"
      }
    ],
    "lastupdate": 1687116861.579437
  },
  "11054": {
    "problemId": "11054",
    "problemLevel": 12,
    "problemName": "가장 긴 바이토닉 부분 수열",
    "average_try": 1.9766,
    "solvedtags": [
      {
        "bojTagId": 25,
        "key": "dp"
      }
    ],
    "lastupdate": 1687116861.579455
  },
  "1937": {
    "problemId": "1937",
    "problemLevel": 13,
    "problemName": "욕심쟁이 판다",
    "average_try": 3.3394,
    "solvedtags": [
      {
        "bojTagId": 127,
        "key": "dfs"
      },
      {
        "bojTagId": 25,
        "key": "dp"
      },
      {
        "bojTagId": 7,
        "key": "graphs"
      },
      {
        "bojTagId": 11,
        "key": "graph_traversal"
      }
    ],
    "lastupdate": 1687116861.579491
  },
  "11066": {
    "problemId": "11066",
    "problemLevel": 13,
    "problemName": "파일 합치기",
    "average_try": 2.0064,
    "solvedtags": [
      {
        "bojTagId": 25,
        "key": "dp"
      }
    ],
    "lastupdate": 1687116861.579508
  },
  "11049": {
    "problemId": "11049",
    "problemLevel": 13,
    "problemName": "행렬 곱셈 순서",
    "average_try": 2.2628,
    "solvedtags": [
      {
        "bojTagId": 25,
        "key": "dp"
      }
    ],
    "lastupdate": 1687116861.579525
  },
  "1958": {
    "problemId": "1958",
    "problemLevel": 13,
    "problemName": "LCS 3",
    "average_try": 2.0009,
    "solvedtags": [
      {
        "bojTagId": 25,
        "key": "dp"
      },
      {
        "bojTagId": 158,
        "key": "string"
      }
    ],
    "lastupdate": 1687116861.57956
  },
  "1727": {
    "problemId": "1727",
    "problemLevel": 14,
    "problemName": "커플 만들기",
    "average_try": 3.2399,
    "solvedtags": [
      {
        "bojTagId": 25,
        "key": "dp"
      },
      {
        "bojTagId": 33,
        "key": "greedy"
      },
      {
        "bojTagId": 97,
        "key": "sorting"
      }
    ],
    "lastupdate": 1687116861.579578
  },
  "1823": {
    "problemId": "1823",
    "problemLevel": 13,
    "problemName": "수확",
    "average_try": 2.1405,
    "solvedtags": [
      {
        "bojTagId": 25,
        "key": "dp"
      }
    ],
    "lastupdate": 1687116861.579595
  },
  "10942": {
    "problemId": "10942",
    "problemLevel": 12,
    "problemName": "팰린드롬?",
    "average_try": 3.3839,
    "solvedtags": [
      {
        "bojTagId": 25,
        "key": "dp"
      }
    ],
    "lastupdate": 1687116861.579613
  },
  "3687": {
    "problemId": "3687",
    "problemLevel": 14,
    "problemName": "성냥개비",
    "average_try": 3.01,
    "solvedtags": [
      {
        "bojTagId": 25,
        "key": "dp"
      },
      {
        "bojTagId": 33,
        "key": "greedy"
      }
    ],
    "lastupdate": 1687116861.579649
  },
  "12015": {
    "problemId": "12015",
    "problemLevel": 14,
    "problemName": "가장 긴 증가하는 부분 수열 2",
    "average_try": 2.4281,
    "solvedtags": [
      {
        "bojTagId": 12,
        "key": "binary_search"
      },
      {
        "bojTagId": 43,
        "key": "lis"
      }
    ],
    "lastupdate": 1687116861.579667
  },
  "11909": {
    "problemId": "11909",
    "problemLevel": 11,
    "problemName": "배열 탈출",
    "average_try": 2.5481,
    "solvedtags": [
      {
        "bojTagId": 22,
        "key": "dijkstra"
      },
      {
        "bojTagId": 25,
        "key": "dp"
      },
      {
        "bojTagId": 7,
        "key": "graphs"
      }
    ],
    "lastupdate": 1687116861.579685
  },
  "21923": {
    "problemId": "21923",
    "problemLevel": 12,
    "problemName": "곡예 비행",
    "average_try": 2.1741,
    "solvedtags": [
      {
        "bojTagId": 25,
        "key": "dp"
      }
    ],
    "lastupdate": 1687116861.579719
  },
  "21941": {
    "problemId": "21941",
    "problemLevel": 12,
    "problemName": "문자열 제거",
    "average_try": 2.592,
    "solvedtags": [
      {
        "bojTagId": 25,
        "key": "dp"
      },
      {
        "bojTagId": 158,
        "key": "string"
      }
    ],
    "lastupdate": 1687116861.579737
  },
  "17831": {
    "problemId": "17831",
    "problemLevel": 16,
    "problemName": "대기업 승범이네",
    "average_try": 2.0739,
    "solvedtags": [
      {
        "bojTagId": 25,
        "key": "dp"
      },
      {
        "bojTagId": 92,
        "key": "dp_tree"
      },
      {
        "bojTagId": 120,
        "key": "trees"
      }
    ],
    "lastupdate": 1687116861.580713
  },
  "1135": {
    "problemId": "1135",
    "problemLevel": 14,
    "problemName": "뉴스 전하기",
    "average_try": 2.1836,
    "solvedtags": [
      {
        "bojTagId": 25,
        "key": "dp"
      },
      {
        "bojTagId": 92,
        "key": "dp_tree"
      },
      {
        "bojTagId": 33,
        "key": "greedy"
      },
      {
        "bojTagId": 97,
        "key": "sorting"
      },
      {
        "bojTagId": 120,
        "key": "trees"
      }
    ],
    "lastupdate": 1687116861.580731
  },
  "1260": {
    "problemId": "1260",
    "problemLevel": 9,
    "problemName": "DFS와 BFS",
    "average_try": 2.7146,
    "solvedtags": [
      {
        "bojTagId": 7,
        "key": "graphs"
      },
      {
        "bojTagId": 11,
        "key": "graph_traversal"
      },
      {
        "bojTagId": 126,
        "key": "bfs"
      },
      {
        "bojTagId": 127,
        "key": "dfs"
      }
    ],
    "lastupdate": 1687116861.581025
  },
  "2606": {
    "problemId": "2606",
    "problemLevel": 8,
    "problemName": "바이러스",
    "average_try": 2.161,
    "solvedtags": [
      {
        "bojTagId": 7,
        "key": "graphs"
      },
      {
        "bojTagId": 11,
        "key": "graph_traversal"
      },
      {
        "bojTagId": 126,
        "key": "bfs"
      },
      {
        "bojTagId": 127,
        "key": "dfs"
      }
    ],
    "lastupdate": 1687116861.58105
  },
  "1012": {
    "problemId": "1012",
    "problemLevel": 9,
    "problemName": "유기농 배추",
    "average_try": 2.6525,
    "solvedtags": [
      {
        "bojTagId": 7,
        "key": "graphs"
      },
      {
        "bojTagId": 11,
        "key": "graph_traversal"
      },
      {
        "bojTagId": 126,
        "key": "bfs"
      },
      {
        "bojTagId": 127,
        "key": "dfs"
      }
    ],
    "lastupdate": 1687116861.581071
  },
  "11724": {
    "problemId": "11724",
    "problemLevel": 9,
    "problemName": "연결 요소의 개수",
    "average_try": 2.3661,
    "solvedtags": [
      {
        "bojTagId": 7,
        "key": "graphs"
      },
      {
        "bojTagId": 11,
        "key": "graph_traversal"
      },
      {
        "bojTagId": 126,
        "key": "bfs"
      },
      {
        "bojTagId": 127,
        "key": "dfs"
      }
    ],
    "lastupdate": 1687116861.58109
  },
  "4963": {
    "problemId": "4963",
    "problemLevel": 9,
    "problemName": "섬의 개수",
    "average_try": 2.0308,
    "solvedtags": [
      {
        "bojTagId": 7,
        "key": "graphs"
      },
      {
        "bojTagId": 11,
        "key": "graph_traversal"
      },
      {
        "bojTagId": 126,
        "key": "bfs"
      },
      {
        "bojTagId": 127,
        "key": "dfs"
      }
    ],
    "lastupdate": 1687116861.581109
  },
  "7562": {
    "problemId": "7562",
    "problemLevel": 10,
    "problemName": "나이트의 이동",
    "average_try": 1.975,
    "solvedtags": [
      {
        "bojTagId": 126,
        "key": "bfs"
      },
      {
        "bojTagId": 7,
        "key": "graphs"
      },
      {
        "bojTagId": 11,
        "key": "graph_traversal"
      }
    ],
    "lastupdate": 1687116861.581135
  },
  "2644": {
    "problemId": "2644",
    "problemLevel": 9,
    "problemName": "촌수계산",
    "average_try": 2.0288,
    "solvedtags": [
      {
        "bojTagId": 7,
        "key": "graphs"
      },
      {
        "bojTagId": 11,
        "key": "graph_traversal"
      },
      {
        "bojTagId": 126,
        "key": "bfs"
      },
      {
        "bojTagId": 127,
        "key": "dfs"
      }
    ],
    "lastupdate": 1687116861.581153
  },
  "1325": {
    "problemId": "1325",
    "problemLevel": 10,
    "problemName": "효율적인 해킹",
    "average_try": 5.1053,
    "solvedtags": [
      {
        "bojTagId": 126,
        "key": "bfs"
      },
      {
        "bojTagId": 127,
        "key": "dfs"
      },
      {
        "bojTagId": 7,
        "key": "graphs"
      },
      {
        "bojTagId": 11,
        "key": "graph_traversal"
      }
    ],
    "lastupdate": 1687116861.58119
  },
  "3184": {
    "problemId": "3184",
    "problemLevel": 10,
    "problemName": "양",
    "average_try": 1.5869,
    "solvedtags": [
      {
        "bojTagId": 126,
        "key": "bfs"
      },
      {
        "bojTagId": 127,
        "key": "dfs"
      },
      {
        "bojTagId": 7,
        "key": "graphs"
      },
      {
        "bojTagId": 11,
        "key": "graph_traversal"
      }
    ],
    "lastupdate": 1687116861.581209
  },
  "16928": {
    "problemId": "16928",
    "problemLevel": 11,
    "problemName": "뱀과 사다리 게임",
    "average_try": 3.009,
    "solvedtags": [
      {
        "bojTagId": 126,
        "key": "bfs"
      },
      {
        "bojTagId": 7,
        "key": "graphs"
      },
      {
        "bojTagId": 11,
        "key": "graph_traversal"
      }
    ],
    "lastupdate": 1687116861.581245
  },
  "13565": {
    "problemId": "13565",
    "problemLevel": 9,
    "problemName": "침투",
    "average_try": 2.2881,
    "solvedtags": [
      {
        "bojTagId": 126,
        "key": "bfs"
      },
      {
        "bojTagId": 127,
        "key": "dfs"
      },
      {
        "bojTagId": 7,
        "key": "graphs"
      },
      {
        "bojTagId": 11,
        "key": "graph_traversal"
      }
    ],
    "lastupdate": 1687116861.581263
  },
  "12761": {
    "problemId": "12761",
    "problemLevel": 10,
    "problemName": "돌다리",
    "average_try": 1.9093,
    "solvedtags": [
      {
        "bojTagId": 126,
        "key": "bfs"
      },
      {
        "bojTagId": 7,
        "key": "graphs"
      },
      {
        "bojTagId": 11,
        "key": "graph_traversal"
      }
    ],
    "lastupdate": 1687116861.581281
  },
  "3187": {
    "problemId": "3187",
    "problemLevel": 10,
    "problemName": "양치기 꿍",
    "average_try": 1.5188,
    "solvedtags": [
      {
        "bojTagId": 126,
        "key": "bfs"
      },
      {
        "bojTagId": 127,
        "key": "dfs"
      },
      {
        "bojTagId": 7,
        "key": "graphs"
      },
      {
        "bojTagId": 11,
        "key": "graph_traversal"
      }
    ],
    "lastupdate": 1687116861.581299
  },
  "18232": {
    "problemId": "18232",
    "problemLevel": 9,
    "problemName": "텔레포트 정거장",
    "average_try": 2.9737,
    "solvedtags": [
      {
        "bojTagId": 126,
        "key": "bfs"
      },
      {
        "bojTagId": 7,
        "key": "graphs"
      },
      {
        "bojTagId": 11,
        "key": "graph_traversal"
      }
    ],
    "lastupdate": 1687116861.581317
  },
  "14248": {
    "problemId": "14248",
    "problemLevel": 9,
    "problemName": "점프 점프",
    "average_try": 1.6776,
    "solvedtags": [
      {
        "bojTagId": 126,
        "key": "bfs"
      },
      {
        "bojTagId": 127,
        "key": "dfs"
      },
      {
        "bojTagId": 7,
        "key": "graphs"
      },
      {
        "bojTagId": 11,
        "key": "graph_traversal"
      }
    ],
    "lastupdate": 1687116861.581334
  },
  "2178": {
    "problemId": "2178",
    "problemLevel": 10,
    "problemName": "미로 탐색",
    "average_try": 2.3249,
    "solvedtags": [
      {
        "bojTagId": 126,
        "key": "bfs"
      },
      {
        "bojTagId": 7,
        "key": "graphs"
      },
      {
        "bojTagId": 11,
        "key": "graph_traversal"
      }
    ],
    "lastupdate": 1687116861.581353
  },
  "2667": {
    "problemId": "2667",
    "problemLevel": 10,
    "problemName": "단지번호붙이기",
    "average_try": 2.3921,
    "solvedtags": [
      {
        "bojTagId": 126,
        "key": "bfs"
      },
      {
        "bojTagId": 127,
        "key": "dfs"
      },
      {
        "bojTagId": 7,
        "key": "graphs"
      },
      {
        "bojTagId": 11,
        "key": "graph_traversal"
      }
    ],
    "lastupdate": 1687116861.581372
  },
  "7576": {
    "problemId": "7576",
    "problemLevel": 11,
    "problemName": "토마토",
    "average_try": 2.7906,
    "solvedtags": [
      {
        "bojTagId": 126,
        "key": "bfs"
      },
      {
        "bojTagId": 7,
        "key": "graphs"
      },
      {
        "bojTagId": 11,
        "key": "graph_traversal"
      }
    ],
    "lastupdate": 1687116861.58139
  },
  "1697": {
    "problemId": "1697",
    "problemLevel": 10,
    "problemName": "숨바꼭질",
    "average_try": 3.9429,
    "solvedtags": [
      {
        "bojTagId": 126,
        "key": "bfs"
      },
      {
        "bojTagId": 7,
        "key": "graphs"
      },
      {
        "bojTagId": 11,
        "key": "graph_traversal"
      }
    ],
    "lastupdate": 1687116861.581408
  },
  "2583": {
    "problemId": "2583",
    "problemLevel": 10,
    "problemName": "영역 구하기",
    "average_try": 1.7444,
    "solvedtags": [
      {
        "bojTagId": 126,
        "key": "bfs"
      },
      {
        "bojTagId": 127,
        "key": "dfs"
      },
      {
        "bojTagId": 7,
        "key": "graphs"
      },
      {
        "bojTagId": 11,
        "key": "graph_traversal"
      }
    ],
    "lastupdate": 1687116861.581426
  },
  "7569": {
    "problemId": "7569",
    "problemLevel": 11,
    "problemName": "토마토",
    "average_try": 2.4061,
    "solvedtags": [
      {
        "bojTagId": 126,
        "key": "bfs"
      },
      {
        "bojTagId": 7,
        "key": "graphs"
      },
      {
        "bojTagId": 11,
        "key": "graph_traversal"
      }
    ],
    "lastupdate": 1687116861.581445
  },
  "5567": {
    "problemId": "5567",
    "problemLevel": 9,
    "problemName": "결혼식",
    "average_try": 2.2847,
    "solvedtags": [
      {
        "bojTagId": 7,
        "key": "graphs"
      },
      {
        "bojTagId": 11,
        "key": "graph_traversal"
      }
    ],
    "lastupdate": 1687116861.581463
  },
  "1926": {
    "problemId": "1926",
    "problemLevel": 10,
    "problemName": "그림",
    "average_try": 2.43,
    "solvedtags": [
      {
        "bojTagId": 126,
        "key": "bfs"
      },
      {
        "bojTagId": 127,
        "key": "dfs"
      },
      {
        "bojTagId": 7,
        "key": "graphs"
      },
      {
        "bojTagId": 11,
        "key": "graph_traversal"
      }
    ],
    "lastupdate": 1687116861.581481
  },
  "1743": {
    "problemId": "1743",
    "problemLevel": 10,
    "problemName": "음식물 피하기",
    "average_try": 2.1332,
    "solvedtags": [
      {
        "bojTagId": 126,
        "key": "bfs"
      },
      {
        "bojTagId": 127,
        "key": "dfs"
      },
      {
        "bojTagId": 7,
        "key": "graphs"
      },
      {
        "bojTagId": 11,
        "key": "graph_traversal"
      }
    ],
    "lastupdate": 1687116861.581499
  },
  "6118": {
    "problemId": "6118",
    "problemLevel": 10,
    "problemName": "숨바꼭질",
    "average_try": 1.8634,
    "solvedtags": [
      {
        "bojTagId": 126,
        "key": "bfs"
      },
      {
        "bojTagId": 7,
        "key": "graphs"
      },
      {
        "bojTagId": 11,
        "key": "graph_traversal"
      }
    ],
    "lastupdate": 1687116861.581517
  },
  "16948": {
    "problemId": "16948",
    "problemLevel": 10,
    "problemName": "데스 나이트",
    "average_try": 1.4462,
    "solvedtags": [
      {
        "bojTagId": 126,
        "key": "bfs"
      },
      {
        "bojTagId": 7,
        "key": "graphs"
      },
      {
        "bojTagId": 11,
        "key": "graph_traversal"
      }
    ],
    "lastupdate": 1687116861.581552
  },
  "16918": {
    "problemId": "16918",
    "problemLevel": 10,
    "problemName": "봄버맨",
    "average_try": 2.4729,
    "solvedtags": [
      {
        "bojTagId": 7,
        "key": "graphs"
      },
      {
        "bojTagId": 11,
        "key": "graph_traversal"
      },
      {
        "bojTagId": 102,
        "key": "implementation"
      },
      {
        "bojTagId": 141,
        "key": "simulation"
      }
    ],
    "lastupdate": 1687116861.58157
  },
  "18405": {
    "problemId": "18405",
    "problemLevel": 11,
    "problemName": "경쟁적 전염",
    "average_try": 3.4399,
    "solvedtags": [
      {
        "bojTagId": 126,
        "key": "bfs"
      },
      {
        "bojTagId": 7,
        "key": "graphs"
      },
      {
        "bojTagId": 11,
        "key": "graph_traversal"
      },
      {
        "bojTagId": 102,
        "key": "implementation"
      }
    ],
    "lastupdate": 1687116861.581588
  },
  "15558": {
    "problemId": "15558",
    "problemLevel": 11,
    "problemName": "점프 게임",
    "average_try": 3.2845,
    "solvedtags": [
      {
        "bojTagId": 126,
        "key": "bfs"
      },
      {
        "bojTagId": 7,
        "key": "graphs"
      },
      {
        "bojTagId": 11,
        "key": "graph_traversal"
      }
    ],
    "lastupdate": 1687116861.581605
  },
  "1303": {
    "problemId": "1303",
    "problemLevel": 10,
    "problemName": "전쟁 - 전투",
    "average_try": 2.6464,
    "solvedtags": [
      {
        "bojTagId": 126,
        "key": "bfs"
      },
      {
        "bojTagId": 127,
        "key": "dfs"
      },
      {
        "bojTagId": 7,
        "key": "graphs"
      },
      {
        "bojTagId": 11,
        "key": "graph_traversal"
      }
    ],
    "lastupdate": 1687116861.581622
  },
  "17086": {
    "problemId": "17086",
    "problemLevel": 9,
    "problemName": "아기 상어 2",
    "average_try": 2.1194,
    "solvedtags": [
      {
        "bojTagId": 126,
        "key": "bfs"
      },
      {
        "bojTagId": 125,
        "key": "bruteforcing"
      },
      {
        "bojTagId": 7,
        "key": "graphs"
      },
      {
        "bojTagId": 11,
        "key": "graph_traversal"
      }
    ],
    "lastupdate": 1687116861.58164
  },
  "14496": {
    "problemId": "14496",
    "problemLevel": 9,
    "problemName": "그대, 그머가 되어",
    "average_try": 2.2086,
    "solvedtags": [
      {
        "bojTagId": 126,
        "key": "bfs"
      },
      {
        "bojTagId": 7,
        "key": "graphs"
      },
      {
        "bojTagId": 11,
        "key": "graph_traversal"
      }
    ],
    "lastupdate": 1687116861.581657
  },
  "11123": {
    "problemId": "11123",
    "problemLevel": 9,
    "problemName": "양 한마리... 양 두마리...",
    "average_try": 1.5344,
    "solvedtags": [
      {
        "bojTagId": 126,
        "key": "bfs"
      },
      {
        "bojTagId": 127,
        "key": "dfs"
      },
      {
        "bojTagId": 7,
        "key": "graphs"
      },
      {
        "bojTagId": 11,
        "key": "graph_traversal"
      }
    ],
    "lastupdate": 1687116861.581675
  },
  "18404": {
    "problemId": "18404",
    "problemLevel": 10,
    "problemName": "현명한 나이트",
    "average_try": 2.0887,
    "solvedtags": [
      {
        "bojTagId": 126,
        "key": "bfs"
      },
      {
        "bojTagId": 7,
        "key": "graphs"
      },
      {
        "bojTagId": 11,
        "key": "graph_traversal"
      }
    ],
    "lastupdate": 1687116861.581694
  },
  "5547": {
    "problemId": "5547",
    "problemLevel": 12,
    "problemName": "일루미네이션",
    "average_try": 1.6544,
    "solvedtags": [
      {
        "bojTagId": 126,
        "key": "bfs"
      },
      {
        "bojTagId": 127,
        "key": "dfs"
      },
      {
        "bojTagId": 7,
        "key": "graphs"
      },
      {
        "bojTagId": 11,
        "key": "graph_traversal"
      }
    ],
    "lastupdate": 1687116861.581712
  },
  "14502": {
    "problemId": "14502",
    "problemLevel": 12,
    "problemName": "연구소",
    "average_try": 1.8239,
    "solvedtags": [
      {
        "bojTagId": 126,
        "key": "bfs"
      },
      {
        "bojTagId": 125,
        "key": "bruteforcing"
      },
      {
        "bojTagId": 7,
        "key": "graphs"
      },
      {
        "bojTagId": 11,
        "key": "graph_traversal"
      },
      {
        "bojTagId": 102,
        "key": "implementation"
      }
    ],
    "lastupdate": 1687116861.58173
  },
  "10026": {
    "problemId": "10026",
    "problemLevel": 11,
    "problemName": "적록색약",
    "average_try": 1.7704,
    "solvedtags": [
      {
        "bojTagId": 126,
        "key": "bfs"
      },
      {
        "bojTagId": 127,
        "key": "dfs"
      },
      {
        "bojTagId": 7,
        "key": "graphs"
      },
      {
        "bojTagId": 11,
        "key": "graph_traversal"
      }
    ],
    "lastupdate": 1687116861.581747
  },
  "3055": {
    "problemId": "3055",
    "problemLevel": 12,
    "problemName": "탈출",
    "average_try": 3.0904,
    "solvedtags": [
      {
        "bojTagId": 126,
        "key": "bfs"
      },
      {
        "bojTagId": 7,
        "key": "graphs"
      },
      {
        "bojTagId": 11,
        "key": "graph_traversal"
      }
    ],
    "lastupdate": 1687116861.581765
  },
  "5014": {
    "problemId": "5014",
    "problemLevel": 10,
    "problemName": "스타트링크",
    "average_try": 3.0155,
    "solvedtags": [
      {
        "bojTagId": 126,
        "key": "bfs"
      },
      {
        "bojTagId": 7,
        "key": "graphs"
      },
      {
        "bojTagId": 11,
        "key": "graph_traversal"
      }
    ],
    "lastupdate": 1687116861.581801
  },
  "2589": {
    "problemId": "2589",
    "problemLevel": 11,
    "problemName": "보물섬",
    "average_try": 2.6606,
    "solvedtags": [
      {
        "bojTagId": 126,
        "key": "bfs"
      },
      {
        "bojTagId": 125,
        "key": "bruteforcing"
      },
      {
        "bojTagId": 7,
        "key": "graphs"
      },
      {
        "bojTagId": 11,
        "key": "graph_traversal"
      }
    ],
    "lastupdate": 1687116861.581819
  },
  "9019": {
    "problemId": "9019",
    "problemLevel": 12,
    "problemName": "DSLR",
    "average_try": 4.7883,
    "solvedtags": [
      {
        "bojTagId": 126,
        "key": "bfs"
      },
      {
        "bojTagId": 7,
        "key": "graphs"
      },
      {
        "bojTagId": 11,
        "key": "graph_traversal"
      }
    ],
    "lastupdate": 1687116861.581837
  },
  "2636": {
    "problemId": "2636",
    "problemLevel": 12,
    "problemName": "치즈",
    "average_try": 1.8384,
    "solvedtags": [
      {
        "bojTagId": 126,
        "key": "bfs"
      },
      {
        "bojTagId": 7,
        "key": "graphs"
      },
      {
        "bojTagId": 11,
        "key": "graph_traversal"
      },
      {
        "bojTagId": 102,
        "key": "implementation"
      },
      {
        "bojTagId": 141,
        "key": "simulation"
      }
    ],
    "lastupdate": 1687116861.581855
  },
  "11559": {
    "problemId": "11559",
    "problemLevel": 12,
    "problemName": "Puyo Puyo",
    "average_try": 2.6211,
    "solvedtags": [
      {
        "bojTagId": 126,
        "key": "bfs"
      },
      {
        "bojTagId": 7,
        "key": "graphs"
      },
      {
        "bojTagId": 11,
        "key": "graph_traversal"
      },
      {
        "bojTagId": 102,
        "key": "implementation"
      },
      {
        "bojTagId": 141,
        "key": "simulation"
      }
    ],
    "lastupdate": 1687116861.58189
  },
  "1600": {
    "problemId": "1600",
    "problemLevel": 13,
    "problemName": "말이 되고픈 원숭이",
    "average_try": 5.008,
    "solvedtags": [
      {
        "bojTagId": 126,
        "key": "bfs"
      },
      {
        "bojTagId": 7,
        "key": "graphs"
      },
      {
        "bojTagId": 11,
        "key": "graph_traversal"
      }
    ],
    "lastupdate": 1687116861.581908
  },
  "12851": {
    "problemId": "12851",
    "problemLevel": 12,
    "problemName": "숨바꼭질 2",
    "average_try": 3.8891,
    "solvedtags": [
      {
        "bojTagId": 126,
        "key": "bfs"
      },
      {
        "bojTagId": 7,
        "key": "graphs"
      },
      {
        "bojTagId": 11,
        "key": "graph_traversal"
      }
    ],
    "lastupdate": 1687116861.581926
  },
  "17141": {
    "problemId": "17141",
    "problemLevel": 12,
    "problemName": "연구소 2",
    "average_try": 2.212,
    "solvedtags": [
      {
        "bojTagId": 126,
        "key": "bfs"
      },
      {
        "bojTagId": 125,
        "key": "bruteforcing"
      },
      {
        "bojTagId": 7,
        "key": "graphs"
      },
      {
        "bojTagId": 11,
        "key": "graph_traversal"
      }
    ],
    "lastupdate": 1687116861.581943
  },
  "16954": {
    "problemId": "16954",
    "problemLevel": 13,
    "problemName": "움직이는 미로 탈출",
    "average_try": 3.566,
    "solvedtags": [
      {
        "bojTagId": 126,
        "key": "bfs"
      },
      {
        "bojTagId": 7,
        "key": "graphs"
      },
      {
        "bojTagId": 11,
        "key": "graph_traversal"
      }
    ],
    "lastupdate": 1687116861.58196
  },
  "14716": {
    "problemId": "14716",
    "problemLevel": 10,
    "problemName": "현수막",
    "average_try": 1.5968,
    "solvedtags": [
      {
        "bojTagId": 126,
        "key": "bfs"
      },
      {
        "bojTagId": 127,
        "key": "dfs"
      },
      {
        "bojTagId": 7,
        "key": "graphs"
      },
      {
        "bojTagId": 11,
        "key": "graph_traversal"
      }
    ],
    "lastupdate": 1687116861.581978
  },
  "17836": {
    "problemId": "17836",
    "problemLevel": 11,
    "problemName": "공주님을 구해라!",
    "average_try": 4.2028,
    "solvedtags": [
      {
        "bojTagId": 126,
        "key": "bfs"
      },
      {
        "bojTagId": 7,
        "key": "graphs"
      },
      {
        "bojTagId": 11,
        "key": "graph_traversal"
      }
    ],
    "lastupdate": 1687116861.581996
  },
  "16973": {
    "problemId": "16973",
    "problemLevel": 12,
    "problemName": "직사각형 탈출",
    "average_try": 3.8457,
    "solvedtags": [
      {
        "bojTagId": 126,
        "key": "bfs"
      },
      {
        "bojTagId": 7,
        "key": "graphs"
      },
      {
        "bojTagId": 11,
        "key": "graph_traversal"
      },
      {
        "bojTagId": 139,
        "key": "prefix_sum"
      }
    ],
    "lastupdate": 1687116861.582013
  },
  "17129": {
    "problemId": "17129",
    "problemLevel": 10,
    "problemName": "윌리암슨수액빨이딱따구리가 정보섬에 올라온 이유",
    "average_try": 2.6667,
    "solvedtags": [
      {
        "bojTagId": 126,
        "key": "bfs"
      },
      {
        "bojTagId": 7,
        "key": "graphs"
      },
      {
        "bojTagId": 11,
        "key": "graph_traversal"
      }
    ],
    "lastupdate": 1687116861.582047
  },
  "16174": {
    "problemId": "16174",
    "problemLevel": 10,
    "problemName": "점프왕 쩰리 (Large)",
    "average_try": 2.1928,
    "solvedtags": [
      {
        "bojTagId": 126,
        "key": "bfs"
      },
      {
        "bojTagId": 127,
        "key": "dfs"
      },
      {
        "bojTagId": 7,
        "key": "graphs"
      },
      {
        "bojTagId": 11,
        "key": "graph_traversal"
      }
    ],
    "lastupdate": 1687116861.582066
  },
  "14940": {
    "problemId": "14940",
    "problemLevel": 10,
    "problemName": "쉬운 최단거리",
    "average_try": 2.5973,
    "solvedtags": [
      {
        "bojTagId": 126,
        "key": "bfs"
      },
      {
        "bojTagId": 7,
        "key": "graphs"
      },
      {
        "bojTagId": 11,
        "key": "graph_traversal"
      }
    ],
    "lastupdate": 1687116861.582084
  },
  "2194": {
    "problemId": "2194",
    "problemLevel": 11,
    "problemName": "유닛 이동시키기",
    "average_try": 3.5212,
    "solvedtags": [
      {
        "bojTagId": 126,
        "key": "bfs"
      },
      {
        "bojTagId": 7,
        "key": "graphs"
      },
      {
        "bojTagId": 11,
        "key": "graph_traversal"
      }
    ],
    "lastupdate": 1687116861.582102
  },
  "18513": {
    "problemId": "18513",
    "problemLevel": 12,
    "problemName": "샘터",
    "average_try": 4.6018,
    "solvedtags": [
      {
        "bojTagId": 126,
        "key": "bfs"
      },
      {
        "bojTagId": 175,
        "key": "data_structures"
      },
      {
        "bojTagId": 7,
        "key": "graphs"
      },
      {
        "bojTagId": 11,
        "key": "graph_traversal"
      }
    ],
    "lastupdate": 1687116861.582119
  },
  "2206": {
    "problemId": "2206",
    "problemLevel": 13,
    "problemName": "벽 부수고 이동하기",
    "average_try": 4.3566,
    "solvedtags": [
      {
        "bojTagId": 126,
        "key": "bfs"
      },
      {
        "bojTagId": 7,
        "key": "graphs"
      },
      {
        "bojTagId": 11,
        "key": "graph_traversal"
      }
    ],
    "lastupdate": 1687116861.582138
  },
  "1707": {
    "problemId": "1707",
    "problemLevel": 12,
    "problemName": "이분 그래프",
    "average_try": 4.1944,
    "solvedtags": [
      {
        "bojTagId": 126,
        "key": "bfs"
      },
      {
        "bojTagId": 197,
        "key": "bipartite_graph"
      },
      {
        "bojTagId": 127,
        "key": "dfs"
      },
      {
        "bojTagId": 7,
        "key": "graphs"
      },
      {
        "bojTagId": 11,
        "key": "graph_traversal"
      }
    ],
    "lastupdate": 1687116861.582156
  },
  "2573": {
    "problemId": "2573",
    "problemLevel": 12,
    "problemName": "빙산",
    "average_try": 3.8937,
    "solvedtags": [
      {
        "bojTagId": 126,
        "key": "bfs"
      },
      {
        "bojTagId": 127,
        "key": "dfs"
      },
      {
        "bojTagId": 7,
        "key": "graphs"
      },
      {
        "bojTagId": 11,
        "key": "graph_traversal"
      },
      {
        "bojTagId": 102,
        "key": "implementation"
      }
    ],
    "lastupdate": 1687116861.582173
  },
  "17142": {
    "problemId": "17142",
    "problemLevel": 13,
    "problemName": "연구소 3",
    "average_try": 3.9294,
    "solvedtags": [
      {
        "bojTagId": 126,
        "key": "bfs"
      },
      {
        "bojTagId": 125,
        "key": "bruteforcing"
      },
      {
        "bojTagId": 7,
        "key": "graphs"
      },
      {
        "bojTagId": 11,
        "key": "graph_traversal"
      }
    ],
    "lastupdate": 1687116861.582191
  },
  "5427": {
    "problemId": "5427",
    "problemLevel": 12,
    "problemName": "불",
    "average_try": 4.1178,
    "solvedtags": [
      {
        "bojTagId": 126,
        "key": "bfs"
      },
      {
        "bojTagId": 7,
        "key": "graphs"
      },
      {
        "bojTagId": 11,
        "key": "graph_traversal"
      }
    ],
    "lastupdate": 1687116861.582209
  },
  "13913": {
    "problemId": "13913",
    "problemLevel": 12,
    "problemName": "숨바꼭질 4",
    "average_try": 3.1902,
    "solvedtags": [
      {
        "bojTagId": 126,
        "key": "bfs"
      },
      {
        "bojTagId": 7,
        "key": "graphs"
      },
      {
        "bojTagId": 11,
        "key": "graph_traversal"
      }
    ],
    "lastupdate": 1687116861.582227
  },
  "2638": {
    "problemId": "2638",
    "problemLevel": 13,
    "problemName": "치즈",
    "average_try": 2.1674,
    "solvedtags": [
      {
        "bojTagId": 126,
        "key": "bfs"
      },
      {
        "bojTagId": 127,
        "key": "dfs"
      },
      {
        "bojTagId": 7,
        "key": "graphs"
      },
      {
        "bojTagId": 11,
        "key": "graph_traversal"
      },
      {
        "bojTagId": 102,
        "key": "implementation"
      },
      {
        "bojTagId": 141,
        "key": "simulation"
      }
    ],
    "lastupdate": 1687116861.582244
  },
  "2665": {
    "problemId": "2665",
    "problemLevel": 12,
    "problemName": "미로만들기",
    "average_try": 1.7763,
    "solvedtags": [
      {
        "bojTagId": 176,
        "key": "0_1_bfs"
      },
      {
        "bojTagId": 126,
        "key": "bfs"
      },
      {
        "bojTagId": 22,
        "key": "dijkstra"
      },
      {
        "bojTagId": 7,
        "key": "graphs"
      },
      {
        "bojTagId": 11,
        "key": "graph_traversal"
      }
    ],
    "lastupdate": 1687116861.582262
  },
  "1726": {
    "problemId": "1726",
    "problemLevel": 13,
    "problemName": "로봇",
    "average_try": 3.9088,
    "solvedtags": [
      {
        "bojTagId": 126,
        "key": "bfs"
      },
      {
        "bojTagId": 7,
        "key": "graphs"
      },
      {
        "bojTagId": 11,
        "key": "graph_traversal"
      }
    ],
    "lastupdate": 1687116861.58228
  },
  "4179": {
    "problemId": "4179",
    "problemLevel": 12,
    "problemName": "불!",
    "average_try": 4.8048,
    "solvedtags": [
      {
        "bojTagId": 126,
        "key": "bfs"
      },
      {
        "bojTagId": 7,
        "key": "graphs"
      },
      {
        "bojTagId": 11,
        "key": "graph_traversal"
      }
    ],
    "lastupdate": 1687116861.582297
  },
  "2234": {
    "problemId": "2234",
    "problemLevel": 13,
    "problemName": "성곽",
    "average_try": 2.1371,
    "solvedtags": [
      {
        "bojTagId": 126,
        "key": "bfs"
      },
      {
        "bojTagId": 14,
        "key": "bitmask"
      },
      {
        "bojTagId": 7,
        "key": "graphs"
      },
      {
        "bojTagId": 11,
        "key": "graph_traversal"
      }
    ],
    "lastupdate": 1687116861.582314
  },
  "6087": {
    "problemId": "6087",
    "problemLevel": 13,
    "problemName": "레이저 통신",
    "average_try": 3.6656,
    "solvedtags": [
      {
        "bojTagId": 126,
        "key": "bfs"
      },
      {
        "bojTagId": 22,
        "key": "dijkstra"
      },
      {
        "bojTagId": 7,
        "key": "graphs"
      },
      {
        "bojTagId": 11,
        "key": "graph_traversal"
      }
    ],
    "lastupdate": 1687116861.582331
  },
  "2151": {
    "problemId": "2151",
    "problemLevel": 13,
    "problemName": "거울 설치",
    "average_try": 4.05,
    "solvedtags": [
      {
        "bojTagId": 126,
        "key": "bfs"
      },
      {
        "bojTagId": 22,
        "key": "dijkstra"
      },
      {
        "bojTagId": 7,
        "key": "graphs"
      },
      {
        "bojTagId": 11,
        "key": "graph_traversal"
      }
    ],
    "lastupdate": 1687116861.582349
  },
  "14923": {
    "problemId": "14923",
    "problemLevel": 12,
    "problemName": "미로 탈출",
    "average_try": 2.5773,
    "solvedtags": [
      {
        "bojTagId": 126,
        "key": "bfs"
      },
      {
        "bojTagId": 7,
        "key": "graphs"
      },
      {
        "bojTagId": 11,
        "key": "graph_traversal"
      }
    ],
    "lastupdate": 1687116861.582366
  },
  "16932": {
    "problemId": "16932",
    "problemLevel": 13,
    "problemName": "모양 만들기",
    "average_try": 2.9775,
    "solvedtags": [
      {
        "bojTagId": 126,
        "key": "bfs"
      },
      {
        "bojTagId": 127,
        "key": "dfs"
      },
      {
        "bojTagId": 7,
        "key": "graphs"
      },
      {
        "bojTagId": 11,
        "key": "graph_traversal"
      }
    ],
    "lastupdate": 1687116861.582384
  },
  "2146": {
    "problemId": "2146",
    "problemLevel": 13,
    "problemName": "다리 만들기",
    "average_try": 2.9798,
    "solvedtags": [
      {
        "bojTagId": 126,
        "key": "bfs"
      },
      {
        "bojTagId": 7,
        "key": "graphs"
      },
      {
        "bojTagId": 11,
        "key": "graph_traversal"
      }
    ],
    "lastupdate": 1687116861.582401
  },
  "14442": {
    "problemId": "14442",
    "problemLevel": 13,
    "problemName": "벽 부수고 이동하기 2",
    "average_try": 3.7154,
    "solvedtags": [
      {
        "bojTagId": 126,
        "key": "bfs"
      },
      {
        "bojTagId": 7,
        "key": "graphs"
      },
      {
        "bojTagId": 11,
        "key": "graph_traversal"
      }
    ],
    "lastupdate": 1687116861.582419
  },
  "10711": {
    "problemId": "10711",
    "problemLevel": 14,
    "problemName": "모래성",
    "average_try": 3.3629,
    "solvedtags": [
      {
        "bojTagId": 126,
        "key": "bfs"
      },
      {
        "bojTagId": 7,
        "key": "graphs"
      },
      {
        "bojTagId": 11,
        "key": "graph_traversal"
      }
    ],
    "lastupdate": 1687116861.582436
  },
  "16947": {
    "problemId": "16947",
    "problemLevel": 13,
    "problemName": "서울 지하철 2호선",
    "average_try": 2.1985,
    "solvedtags": [
      {
        "bojTagId": 126,
        "key": "bfs"
      },
      {
        "bojTagId": 127,
        "key": "dfs"
      },
      {
        "bojTagId": 7,
        "key": "graphs"
      },
      {
        "bojTagId": 11,
        "key": "graph_traversal"
      }
    ],
    "lastupdate": 1687116861.582454
  },
  "16988": {
    "problemId": "16988",
    "problemLevel": 13,
    "problemName": "Baaaaaaaaaduk2 (Easy)",
    "average_try": 2.0053,
    "solvedtags": [
      {
        "bojTagId": 126,
        "key": "bfs"
      },
      {
        "bojTagId": 125,
        "key": "bruteforcing"
      },
      {
        "bojTagId": 127,
        "key": "dfs"
      },
      {
        "bojTagId": 7,
        "key": "graphs"
      },
      {
        "bojTagId": 11,
        "key": "graph_traversal"
      }
    ],
    "lastupdate": 1687116861.582471
  },
  "16985": {
    "problemId": "16985",
    "problemLevel": 14,
    "problemName": "Maaaaaaaaaze",
    "average_try": 1.7811,
    "solvedtags": [
      {
        "bojTagId": 126,
        "key": "bfs"
      },
      {
        "bojTagId": 125,
        "key": "bruteforcing"
      },
      {
        "bojTagId": 7,
        "key": "graphs"
      },
      {
        "bojTagId": 11,
        "key": "graph_traversal"
      },
      {
        "bojTagId": 102,
        "key": "implementation"
      }
    ],
    "lastupdate": 1687116861.582489
  },
  "16956": {
    "problemId": "16956",
    "problemLevel": 8,
    "problemName": "늑대와 양",
    "average_try": 2.0994,
    "solvedtags": [
      {
        "bojTagId": 109,
        "key": "ad_hoc"
      },
      {
        "bojTagId": 128,
        "key": "constructive"
      }
    ],
    "lastupdate": 1687116861.582507
  },
  "2668": {
    "problemId": "2668",
    "problemLevel": 11,
    "problemName": "숫자고르기",
    "average_try": 2.2013,
    "solvedtags": [
      {
        "bojTagId": 127,
        "key": "dfs"
      },
      {
        "bojTagId": 7,
        "key": "graphs"
      },
      {
        "bojTagId": 11,
        "key": "graph_traversal"
      }
    ],
    "lastupdate": 1687116861.58256
  },
  "13023": {
    "problemId": "13023",
    "problemLevel": 11,
    "problemName": "ABCDE",
    "average_try": 3.4841,
    "solvedtags": [
      {
        "bojTagId": 5,
        "key": "backtracking"
      },
      {
        "bojTagId": 127,
        "key": "dfs"
      },
      {
        "bojTagId": 7,
        "key": "graphs"
      },
      {
        "bojTagId": 11,
        "key": "graph_traversal"
      }
    ],
    "lastupdate": 1687116861.582578
  },
  "16432": {
    "problemId": "16432",
    "problemLevel": 12,
    "problemName": "떡장수와 호랑이",
    "average_try": 3.6204,
    "solvedtags": [
      {
        "bojTagId": 127,
        "key": "dfs"
      },
      {
        "bojTagId": 25,
        "key": "dp"
      },
      {
        "bojTagId": 7,
        "key": "graphs"
      },
      {
        "bojTagId": 11,
        "key": "graph_traversal"
      }
    ],
    "lastupdate": 1687116861.582595
  },
  "9466": {
    "problemId": "9466",
    "problemLevel": 13,
    "problemName": "텀 프로젝트",
    "average_try": 4.1661,
    "solvedtags": [
      {
        "bojTagId": 127,
        "key": "dfs"
      },
      {
        "bojTagId": 7,
        "key": "graphs"
      },
      {
        "bojTagId": 11,
        "key": "graph_traversal"
      }
    ],
    "lastupdate": 1687116861.582612
  },
  "17616": {
    "problemId": "17616",
    "problemLevel": 13,
    "problemName": "등수 찾기",
    "average_try": 2.1308,
    "solvedtags": [
      {
        "bojTagId": 126,
        "key": "bfs"
      },
      {
        "bojTagId": 127,
        "key": "dfs"
      },
      {
        "bojTagId": 7,
        "key": "graphs"
      },
      {
        "bojTagId": 11,
        "key": "graph_traversal"
      }
    ],
    "lastupdate": 1687116861.582647
  },
  "21937": {
    "problemId": "21937",
    "problemLevel": 10,
    "problemName": "작업",
    "average_try": 1.9783,
    "solvedtags": [
      {
        "bojTagId": 127,
        "key": "dfs"
      },
      {
        "bojTagId": 7,
        "key": "graphs"
      },
      {
        "bojTagId": 11,
        "key": "graph_traversal"
      }
    ],
    "lastupdate": 1687116861.582665
  },
  "21938": {
    "problemId": "21938",
    "problemLevel": 9,
    "problemName": "영상처리",
    "average_try": 2.683,
    "solvedtags": [
      {
        "bojTagId": 126,
        "key": "bfs"
      },
      {
        "bojTagId": 127,
        "key": "dfs"
      },
      {
        "bojTagId": 7,
        "key": "graphs"
      },
      {
        "bojTagId": 11,
        "key": "graph_traversal"
      }
    ],
    "lastupdate": 1687116861.582683
  },
  "22868": {
    "problemId": "22868",
    "problemLevel": 13,
    "problemName": "산책 (small)",
    "average_try": 3.4885,
    "solvedtags": [
      {
        "bojTagId": 126,
        "key": "bfs"
      },
      {
        "bojTagId": 7,
        "key": "graphs"
      },
      {
        "bojTagId": 11,
        "key": "graph_traversal"
      }
    ],
    "lastupdate": 1687116861.5827
  },
  "22946": {
    "problemId": "22946",
    "problemLevel": 14,
    "problemName": "원 이동하기 1",
    "average_try": 5.4118,
    "solvedtags": [
      {
        "bojTagId": 127,
        "key": "dfs"
      },
      {
        "bojTagId": 100,
        "key": "geometry"
      },
      {
        "bojTagId": 7,
        "key": "graphs"
      },
      {
        "bojTagId": 11,
        "key": "graph_traversal"
      },
      {
        "bojTagId": 97,
        "key": "sorting"
      },
      {
        "bojTagId": 120,
        "key": "trees"
      }
    ],
    "lastupdate": 1687116861.582718
  },
  "22948": {
    "problemId": "22948",
    "problemLevel": 13,
    "problemName": "원 이동하기 2",
    "average_try": 2.6216,
    "solvedtags": [
      {
        "bojTagId": 126,
        "key": "bfs"
      },
      {
        "bojTagId": 175,
        "key": "data_structures"
      },
      {
        "bojTagId": 7,
        "key": "graphs"
      },
      {
        "bojTagId": 11,
        "key": "graph_traversal"
      },
      {
        "bojTagId": 71,
        "key": "stack"
      }
    ],
    "lastupdate": 1687116861.582735
  },
  "22949": {
    "problemId": "22949",
    "problemLevel": 16,
    "problemName": "회전 미로 탐색",
    "average_try": 2.7692,
    "solvedtags": [
      {
        "bojTagId": 126,
        "key": "bfs"
      },
      {
        "bojTagId": 7,
        "key": "graphs"
      },
      {
        "bojTagId": 11,
        "key": "graph_traversal"
      },
      {
        "bojTagId": 102,
        "key": "implementation"
      },
      {
        "bojTagId": 141,
        "key": "simulation"
      }
    ],
    "lastupdate": 1687116861.582753
  },
  "11000": {
    "problemId": "11000",
    "problemLevel": 11,
    "problemName": "강의실 배정",
    "average_try": 3.4636,
    "solvedtags": [
      {
        "bojTagId": 175,
        "key": "data_structures"
      },
      {
        "bojTagId": 33,
        "key": "greedy"
      },
      {
        "bojTagId": 59,
        "key": "priority_queue"
      },
      {
        "bojTagId": 97,
        "key": "sorting"
      }
    ],
    "lastupdate": 1687116861.583709
  },
  "13164": {
    "problemId": "13164",
    "problemLevel": 11,
    "problemName": "행복 유치원",
    "average_try": 1.8126,
    "solvedtags": [
      {
        "bojTagId": 33,
        "key": "greedy"
      },
      {
        "bojTagId": 97,
        "key": "sorting"
      }
    ],
    "lastupdate": 1687116861.583733
  },
  "1931": {
    "problemId": "1931",
    "problemLevel": 10,
    "problemName": "회의실 배정",
    "average_try": 3.3432,
    "solvedtags": [
      {
        "bojTagId": 33,
        "key": "greedy"
      },
      {
        "bojTagId": 97,
        "key": "sorting"
      }
    ],
    "lastupdate": 1687116861.583753
  },
  "14916": {
    "problemId": "14916",
    "problemLevel": 6,
    "problemName": "거스름돈",
    "average_try": 2.1161,
    "solvedtags": [
      {
        "bojTagId": 25,
        "key": "dp"
      },
      {
        "bojTagId": 33,
        "key": "greedy"
      },
      {
        "bojTagId": 124,
        "key": "math"
      }
    ],
    "lastupdate": 1687116861.583772
  },
  "1439": {
    "problemId": "1439",
    "problemLevel": 6,
    "problemName": "뒤집기",
    "average_try": 1.8088,
    "solvedtags": [
      {
        "bojTagId": 33,
        "key": "greedy"
      },
      {
        "bojTagId": 158,
        "key": "string"
      }
    ],
    "lastupdate": 1687116861.58379
  },
  "17521": {
    "problemId": "17521",
    "problemLevel": 7,
    "problemName": "Byte Coin",
    "average_try": 2.4469,
    "solvedtags": [
      {
        "bojTagId": 33,
        "key": "greedy"
      }
    ],
    "lastupdate": 1687116861.583808
  },
  "19939": {
    "problemId": "19939",
    "problemLevel": 7,
    "problemName": "박 터뜨리기",
    "average_try": 2.6681,
    "solvedtags": [
      {
        "bojTagId": 33,
        "key": "greedy"
      },
      {
        "bojTagId": 124,
        "key": "math"
      }
    ],
    "lastupdate": 1687116861.583838
  },
  "12782": {
    "problemId": "12782",
    "problemLevel": 7,
    "problemName": "비트 우정지수",
    "average_try": 1.4493,
    "solvedtags": [
      {
        "bojTagId": 33,
        "key": "greedy"
      },
      {
        "bojTagId": 124,
        "key": "math"
      }
    ],
    "lastupdate": 1687116861.583856
  },
  "16208": {
    "problemId": "16208",
    "problemLevel": 6,
    "problemName": "귀찮음",
    "average_try": 1.933,
    "solvedtags": [
      {
        "bojTagId": 33,
        "key": "greedy"
      },
      {
        "bojTagId": 124,
        "key": "math"
      },
      {
        "bojTagId": 97,
        "key": "sorting"
      }
    ],
    "lastupdate": 1687116861.583874
  },
  "11256": {
    "problemId": "11256",
    "problemLevel": 6,
    "problemName": "사탕",
    "average_try": 1.489,
    "solvedtags": [
      {
        "bojTagId": 33,
        "key": "greedy"
      },
      {
        "bojTagId": 97,
        "key": "sorting"
      }
    ],
    "lastupdate": 1687116861.583892
  },
  "13019": {
    "problemId": "13019",
    "problemLevel": 12,
    "problemName": "A를 B로",
    "average_try": 2.2429,
    "solvedtags": [
      {
        "bojTagId": 33,
        "key": "greedy"
      }
    ],
    "lastupdate": 1687116861.58391
  },
  "2217": {
    "problemId": "2217",
    "problemLevel": 7,
    "problemName": "로프",
    "average_try": 2.3359,
    "solvedtags": [
      {
        "bojTagId": 33,
        "key": "greedy"
      },
      {
        "bojTagId": 124,
        "key": "math"
      },
      {
        "bojTagId": 97,
        "key": "sorting"
      }
    ],
    "lastupdate": 1687116861.583928
  },
  "13305": {
    "problemId": "13305",
    "problemLevel": 8,
    "problemName": "주유소",
    "average_try": 2.6233,
    "solvedtags": [
      {
        "bojTagId": 33,
        "key": "greedy"
      }
    ],
    "lastupdate": 1687116861.583946
  },
  "2847": {
    "problemId": "2847",
    "problemLevel": 7,
    "problemName": "게임을 만든 동준이",
    "average_try": 1.8485,
    "solvedtags": [
      {
        "bojTagId": 33,
        "key": "greedy"
      }
    ],
    "lastupdate": 1687116861.583964
  },
  "1343": {
    "problemId": "1343",
    "problemLevel": 6,
    "problemName": "폴리오미노",
    "average_try": 1.8685,
    "solvedtags": [
      {
        "bojTagId": 33,
        "key": "greedy"
      },
      {
        "bojTagId": 102,
        "key": "implementation"
      }
    ],
    "lastupdate": 1687116861.583982
  },
  "13413": {
    "problemId": "13413",
    "problemLevel": 7,
    "problemName": "오셀로 재배치",
    "average_try": 1.7742,
    "solvedtags": [
      {
        "bojTagId": 33,
        "key": "greedy"
      },
      {
        "bojTagId": 158,
        "key": "string"
      }
    ],
    "lastupdate": 1687116861.584
  },
  "1758": {
    "problemId": "1758",
    "problemLevel": 7,
    "problemName": "알바생 강호",
    "average_try": 2.322,
    "solvedtags": [
      {
        "bojTagId": 33,
        "key": "greedy"
      },
      {
        "bojTagId": 97,
        "key": "sorting"
      }
    ],
    "lastupdate": 1687116861.584018
  },
  "16162": {
    "problemId": "16162",
    "problemLevel": 7,
    "problemName": "가희와 3단 고음",
    "average_try": 1.5991,
    "solvedtags": [
      {
        "bojTagId": 33,
        "key": "greedy"
      }
    ],
    "lastupdate": 1687116861.584036
  },
  "16435": {
    "problemId": "16435",
    "problemLevel": 6,
    "problemName": "스네이크버드",
    "average_try": 1.365,
    "solvedtags": [
      {
        "bojTagId": 33,
        "key": "greedy"
      },
      {
        "bojTagId": 97,
        "key": "sorting"
      }
    ],
    "lastupdate": 1687116861.584054
  },
  "11399": {
    "problemId": "11399",
    "problemLevel": 7,
    "problemName": "ATM",
    "average_try": 1.4707,
    "solvedtags": [
      {
        "bojTagId": 33,
        "key": "greedy"
      },
      {
        "bojTagId": 97,
        "key": "sorting"
      }
    ],
    "lastupdate": 1687116861.584071
  },
  "1449": {
    "problemId": "1449",
    "problemLevel": 8,
    "problemName": "수리공 항승",
    "average_try": 2.1224,
    "solvedtags": [
      {
        "bojTagId": 33,
        "key": "greedy"
      },
      {
        "bojTagId": 97,
        "key": "sorting"
      }
    ],
    "lastupdate": 1687116861.584089
  },
  "11508": {
    "problemId": "11508",
    "problemLevel": 7,
    "problemName": "2+1 세일",
    "average_try": 1.6838,
    "solvedtags": [
      {
        "bojTagId": 33,
        "key": "greedy"
      },
      {
        "bojTagId": 97,
        "key": "sorting"
      }
    ],
    "lastupdate": 1687116861.584107
  },
  "1817": {
    "problemId": "1817",
    "problemLevel": 6,
    "problemName": "짐 챙기는 숌",
    "average_try": 2.2827,
    "solvedtags": [
      {
        "bojTagId": 33,
        "key": "greedy"
      },
      {
        "bojTagId": 102,
        "key": "implementation"
      }
    ],
    "lastupdate": 1687116861.584124
  },
  "20115": {
    "problemId": "20115",
    "problemLevel": 8,
    "problemName": "에너지 드링크",
    "average_try": 1.3786,
    "solvedtags": [
      {
        "bojTagId": 33,
        "key": "greedy"
      }
    ],
    "lastupdate": 1687116861.584142
  },
  "20300": {
    "problemId": "20300",
    "problemLevel": 8,
    "problemName": "서강근육맨",
    "average_try": 2.7606,
    "solvedtags": [
      {
        "bojTagId": 33,
        "key": "greedy"
      },
      {
        "bojTagId": 97,
        "key": "sorting"
      }
    ],
    "lastupdate": 1687116861.58416
  },
  "14247": {
    "problemId": "14247",
    "problemLevel": 9,
    "problemName": "나무 자르기",
    "average_try": 2.2996,
    "solvedtags": [
      {
        "bojTagId": 33,
        "key": "greedy"
      },
      {
        "bojTagId": 97,
        "key": "sorting"
      }
    ],
    "lastupdate": 1687116861.584178
  },
  "1541": {
    "problemId": "1541",
    "problemLevel": 9,
    "problemName": "잃어버린 괄호",
    "average_try": 1.901,
    "solvedtags": [
      {
        "bojTagId": 33,
        "key": "greedy"
      },
      {
        "bojTagId": 124,
        "key": "math"
      },
      {
        "bojTagId": 96,
        "key": "parsing"
      },
      {
        "bojTagId": 158,
        "key": "string"
      }
    ],
    "lastupdate": 1687116861.584195
  },
  "1080": {
    "problemId": "1080",
    "problemLevel": 10,
    "problemName": "행렬",
    "average_try": 2.3921,
    "solvedtags": [
      {
        "bojTagId": 33,
        "key": "greedy"
      }
    ],
    "lastupdate": 1687116861.584213
  },
  "2138": {
    "problemId": "2138",
    "problemLevel": 11,
    "problemName": "전구와 스위치",
    "average_try": 2.6421,
    "solvedtags": [
      {
        "bojTagId": 33,
        "key": "greedy"
      }
    ],
    "lastupdate": 1687116861.58423
  },
  "20365": {
    "problemId": "20365",
    "problemLevel": 8,
    "problemName": "블로그2",
    "average_try": 2.1971,
    "solvedtags": [
      {
        "bojTagId": 33,
        "key": "greedy"
      },
      {
        "bojTagId": 158,
        "key": "string"
      }
    ],
    "lastupdate": 1687116861.584248
  },
  "14400": {
    "problemId": "14400",
    "problemLevel": 9,
    "problemName": "편의점 2",
    "average_try": 2.3988,
    "solvedtags": [
      {
        "bojTagId": 100,
        "key": "geometry"
      },
      {
        "bojTagId": 124,
        "key": "math"
      },
      {
        "bojTagId": 97,
        "key": "sorting"
      }
    ],
    "lastupdate": 1687116861.584266
  },
  "11047": {
    "problemId": "11047",
    "problemLevel": 7,
    "problemName": "동전 0",
    "average_try": 1.9232,
    "solvedtags": [
      {
        "bojTagId": 33,
        "key": "greedy"
      }
    ],
    "lastupdate": 1687116861.584283
  },
  "1946": {
    "problemId": "1946",
    "problemLevel": 10,
    "problemName": "신입 사원",
    "average_try": 3.0862,
    "solvedtags": [
      {
        "bojTagId": 33,
        "key": "greedy"
      },
      {
        "bojTagId": 97,
        "key": "sorting"
      }
    ],
    "lastupdate": 1687116861.5843
  },
  "16953": {
    "problemId": "16953",
    "problemLevel": 9,
    "problemName": "A → B",
    "average_try": 2.5063,
    "solvedtags": [
      {
        "bojTagId": 126,
        "key": "bfs"
      },
      {
        "bojTagId": 7,
        "key": "graphs"
      },
      {
        "bojTagId": 11,
        "key": "graph_traversal"
      },
      {
        "bojTagId": 33,
        "key": "greedy"
      }
    ],
    "lastupdate": 1687116861.584318
  },
  "11509": {
    "problemId": "11509",
    "problemLevel": 11,
    "problemName": "풍선 맞추기",
    "average_try": 2.7165,
    "solvedtags": [
      {
        "bojTagId": 33,
        "key": "greedy"
      }
    ],
    "lastupdate": 1687116861.584335
  },
  "17615": {
    "problemId": "17615",
    "problemLevel": 10,
    "problemName": "볼 모으기",
    "average_try": 2.4795,
    "solvedtags": [
      {
        "bojTagId": 33,
        "key": "greedy"
      }
    ],
    "lastupdate": 1687116861.584352
  },
  "19539": {
    "problemId": "19539",
    "problemLevel": 11,
    "problemName": "사과나무",
    "average_try": 2.2937,
    "solvedtags": [
      {
        "bojTagId": 33,
        "key": "greedy"
      },
      {
        "bojTagId": 124,
        "key": "math"
      }
    ],
    "lastupdate": 1687116861.584369
  },
  "1474": {
    "problemId": "1474",
    "problemLevel": 10,
    "problemName": "밑 줄",
    "average_try": 2.2966,
    "solvedtags": [
      {
        "bojTagId": 5,
        "key": "backtracking"
      },
      {
        "bojTagId": 125,
        "key": "bruteforcing"
      },
      {
        "bojTagId": 33,
        "key": "greedy"
      },
      {
        "bojTagId": 158,
        "key": "string"
      }
    ],
    "lastupdate": 1687116861.584387
  },
  "1455": {
    "problemId": "1455",
    "problemLevel": 9,
    "problemName": "뒤집기 II",
    "average_try": 1.6619,
    "solvedtags": [
      {
        "bojTagId": 33,
        "key": "greedy"
      }
    ],
    "lastupdate": 1687116861.584404
  },
  "16206": {
    "problemId": "16206",
    "problemLevel": 10,
    "problemName": "롤케이크",
    "average_try": 3.3361,
    "solvedtags": [
      {
        "bojTagId": 33,
        "key": "greedy"
      }
    ],
    "lastupdate": 1687116861.584421
  },
  "2141": {
    "problemId": "2141",
    "problemLevel": 12,
    "problemName": "우체국",
    "average_try": 3.961,
    "solvedtags": [
      {
        "bojTagId": 33,
        "key": "greedy"
      },
      {
        "bojTagId": 97,
        "key": "sorting"
      }
    ],
    "lastupdate": 1687116861.584439
  },
  "19598": {
    "problemId": "19598",
    "problemLevel": 11,
    "problemName": "최소 회의실 개수",
    "average_try": 2.3633,
    "solvedtags": [
      {
        "bojTagId": 175,
        "key": "data_structures"
      },
      {
        "bojTagId": 33,
        "key": "greedy"
      },
      {
        "bojTagId": 59,
        "key": "priority_queue"
      },
      {
        "bojTagId": 97,
        "key": "sorting"
      },
      {
        "bojTagId": 106,
        "key": "sweeping"
      }
    ],
    "lastupdate": 1687116861.584457
  },
  "20117": {
    "problemId": "20117",
    "problemLevel": 10,
    "problemName": "호반우 상인의 이상한 품질 계산법",
    "average_try": 1.646,
    "solvedtags": [
      {
        "bojTagId": 33,
        "key": "greedy"
      },
      {
        "bojTagId": 97,
        "key": "sorting"
      }
    ],
    "lastupdate": 1687116861.584474
  },
  "2812": {
    "problemId": "2812",
    "problemLevel": 13,
    "problemName": "크게 만들기",
    "average_try": 3.7681,
    "solvedtags": [
      {
        "bojTagId": 175,
        "key": "data_structures"
      },
      {
        "bojTagId": 33,
        "key": "greedy"
      },
      {
        "bojTagId": 71,
        "key": "stack"
      }
    ],
    "lastupdate": 1687116861.584492
  },
  "2212": {
    "problemId": "2212",
    "problemLevel": 11,
    "problemName": "센서",
    "average_try": 2.0588,
    "solvedtags": [
      {
        "bojTagId": 33,
        "key": "greedy"
      },
      {
        "bojTagId": 97,
        "key": "sorting"
      }
    ],
    "lastupdate": 1687116861.58451
  },
  "1092": {
    "problemId": "1092",
    "problemLevel": 11,
    "problemName": "배",
    "average_try": 4.1794,
    "solvedtags": [
      {
        "bojTagId": 33,
        "key": "greedy"
      },
      {
        "bojTagId": 97,
        "key": "sorting"
      }
    ],
    "lastupdate": 1687116861.584527
  },
  "1374": {
    "problemId": "1374",
    "problemLevel": 11,
    "problemName": "강의실",
    "average_try": 2.2173,
    "solvedtags": [
      {
        "bojTagId": 175,
        "key": "data_structures"
      },
      {
        "bojTagId": 33,
        "key": "greedy"
      },
      {
        "bojTagId": 59,
        "key": "priority_queue"
      },
      {
        "bojTagId": 97,
        "key": "sorting"
      }
    ],
    "lastupdate": 1687116861.584545
  },
  "13975": {
    "problemId": "13975",
    "problemLevel": 12,
    "problemName": "파일 합치기 3",
    "average_try": 2.0876,
    "solvedtags": [
      {
        "bojTagId": 175,
        "key": "data_structures"
      },
      {
        "bojTagId": 33,
        "key": "greedy"
      },
      {
        "bojTagId": 59,
        "key": "priority_queue"
      }
    ],
    "lastupdate": 1687116861.584563
  },
  "6068": {
    "problemId": "6068",
    "problemLevel": 11,
    "problemName": "시간 관리하기",
    "average_try": 1.8875,
    "solvedtags": [
      {
        "bojTagId": 33,
        "key": "greedy"
      },
      {
        "bojTagId": 97,
        "key": "sorting"
      }
    ],
    "lastupdate": 1687116861.58458
  },
  "1744": {
    "problemId": "1744",
    "problemLevel": 12,
    "problemName": "수 묶기",
    "average_try": 3.1828,
    "solvedtags": [
      {
        "bojTagId": 137,
        "key": "case_work"
      },
      {
        "bojTagId": 33,
        "key": "greedy"
      },
      {
        "bojTagId": 97,
        "key": "sorting"
      }
    ],
    "lastupdate": 1687116861.584597
  },
  "1715": {
    "problemId": "1715",
    "problemLevel": 12,
    "problemName": "카드 정렬하기",
    "average_try": 2.975,
    "solvedtags": [
      {
        "bojTagId": 175,
        "key": "data_structures"
      },
      {
        "bojTagId": 33,
        "key": "greedy"
      },
      {
        "bojTagId": 59,
        "key": "priority_queue"
      }
    ],
    "lastupdate": 1687116861.584614
  },
  "8980": {
    "problemId": "8980",
    "problemLevel": 14,
    "problemName": "택배",
    "average_try": 2.3751,
    "solvedtags": [
      {
        "bojTagId": 33,
        "key": "greedy"
      },
      {
        "bojTagId": 97,
        "key": "sorting"
      }
    ],
    "lastupdate": 1687116861.584632
  },
  "2457": {
    "problemId": "2457",
    "problemLevel": 13,
    "problemName": "공주님의 정원",
    "average_try": 3.9,
    "solvedtags": [
      {
        "bojTagId": 33,
        "key": "greedy"
      },
      {
        "bojTagId": 97,
        "key": "sorting"
      }
    ],
    "lastupdate": 1687116861.584649
  },
  "2109": {
    "problemId": "2109",
    "problemLevel": 13,
    "problemName": "순회강연",
    "average_try": 2.6692,
    "solvedtags": [
      {
        "bojTagId": 175,
        "key": "data_structures"
      },
      {
        "bojTagId": 33,
        "key": "greedy"
      },
      {
        "bojTagId": 59,
        "key": "priority_queue"
      },
      {
        "bojTagId": 97,
        "key": "sorting"
      }
    ],
    "lastupdate": 1687116861.584667
  },
  "1082": {
    "problemId": "1082",
    "problemLevel": 13,
    "problemName": "방 번호",
    "average_try": 3.2761,
    "solvedtags": [
      {
        "bojTagId": 25,
        "key": "dp"
      },
      {
        "bojTagId": 33,
        "key": "greedy"
      }
    ],
    "lastupdate": 1687116861.584684
  },
  "12931": {
    "problemId": "12931",
    "problemLevel": 11,
    "problemName": "두 배 더하기",
    "average_try": 1.6271,
    "solvedtags": [
      {
        "bojTagId": 33,
        "key": "greedy"
      }
    ],
    "lastupdate": 1687116861.584702
  },
  "18234": {
    "problemId": "18234",
    "problemLevel": 13,
    "problemName": "당근 훔쳐 먹기",
    "average_try": 2.3386,
    "solvedtags": [
      {
        "bojTagId": 33,
        "key": "greedy"
      },
      {
        "bojTagId": 97,
        "key": "sorting"
      }
    ],
    "lastupdate": 1687116861.58472
  },
  "2285": {
    "problemId": "2285",
    "problemLevel": 12,
    "problemName": "우체국",
    "average_try": 2.934,
    "solvedtags": [
      {
        "bojTagId": 33,
        "key": "greedy"
      }
    ],
    "lastupdate": 1687116861.584737
  },
  "21313": {
    "problemId": "21313",
    "problemLevel": 4,
    "problemName": "문어",
    "average_try": 1.4314,
    "solvedtags": [
      {
        "bojTagId": 109,
        "key": "ad_hoc"
      },
      {
        "bojTagId": 33,
        "key": "greedy"
      }
    ],
    "lastupdate": 1687116861.584754
  },
  "21314": {
    "problemId": "21314",
    "problemLevel": 9,
    "problemName": "민겸 수",
    "average_try": 2.8906,
    "solvedtags": [
      {
        "bojTagId": 33,
        "key": "greedy"
      },
      {
        "bojTagId": 102,
        "key": "implementation"
      }
    ],
    "lastupdate": 1687116861.584771
  },
  "21758": {
    "problemId": "21758",
    "problemLevel": 11,
    "problemName": "꿀 따기",
    "average_try": 2.6667,
    "solvedtags": [
      {
        "bojTagId": 137,
        "key": "case_work"
      },
      {
        "bojTagId": 33,
        "key": "greedy"
      },
      {
        "bojTagId": 139,
        "key": "prefix_sum"
      }
    ],
    "lastupdate": 1687116861.584788
  },
  "21925": {
    "problemId": "21925",
    "problemLevel": 13,
    "problemName": "짝수 팰린드롬",
    "average_try": 2.7381,
    "solvedtags": [
      {
        "bojTagId": 25,
        "key": "dp"
      },
      {
        "bojTagId": 33,
        "key": "greedy"
      }
    ],
    "lastupdate": 1687116861.584806
  },
  "1212": {
    "problemId": "1212",
    "problemLevel": 4,
    "problemName": "8진수 2진수",
    "average_try": 2.791,
    "solvedtags": [
      {
        "bojTagId": 102,
        "key": "implementation"
      },
      {
        "bojTagId": 124,
        "key": "math"
      },
      {
        "bojTagId": 158,
        "key": "string"
      }
    ],
    "lastupdate": 1687116861.585489
  },
  "2753": {
    "problemId": "2753",
    "problemLevel": 1,
    "problemName": "윤년",
    "average_try": 1.9165,
    "solvedtags": [
      {
        "bojTagId": 102,
        "key": "implementation"
      },
      {
        "bojTagId": 121,
        "key": "arithmetic"
      },
      {
        "bojTagId": 124,
        "key": "math"
      }
    ],
    "lastupdate": 1687116861.585515
  },
  "20053": {
    "problemId": "20053",
    "problemLevel": 3,
    "problemName": "최소, 최대 2",
    "average_try": 1.6672,
    "solvedtags": [
      {
        "bojTagId": 102,
        "key": "implementation"
      }
    ],
    "lastupdate": 1687116861.585535
  },
  "5597": {
    "problemId": "5597",
    "problemLevel": 1,
    "problemName": "과제 안 내신 분..?",
    "average_try": 1.8755,
    "solvedtags": [
      {
        "bojTagId": 102,
        "key": "implementation"
      }
    ],
    "lastupdate": 1687116861.585553
  },
  "20546": {
    "problemId": "20546",
    "problemLevel": 6,
    "problemName": "🐜 기적의 매매법 🐜",
    "average_try": 2.1442,
    "solvedtags": [
      {
        "bojTagId": 102,
        "key": "implementation"
      }
    ],
    "lastupdate": 1687116861.585571
  },
  "1913": {
    "problemId": "1913",
    "problemLevel": 8,
    "problemName": "달팽이",
    "average_try": 2.1476,
    "solvedtags": [
      {
        "bojTagId": 102,
        "key": "implementation"
      }
    ],
    "lastupdate": 1687116861.585609
  },
  "14467": {
    "problemId": "14467",
    "problemLevel": 5,
    "problemName": "소가 길을 건너간 이유 1",
    "average_try": 1.6602,
    "solvedtags": [
      {
        "bojTagId": 102,
        "key": "implementation"
      }
    ],
    "lastupdate": 1687116861.585627
  },
  "2578": {
    "problemId": "2578",
    "problemLevel": 7,
    "problemName": "빙고",
    "average_try": 2.1997,
    "solvedtags": [
      {
        "bojTagId": 102,
        "key": "implementation"
      },
      {
        "bojTagId": 141,
        "key": "simulation"
      }
    ],
    "lastupdate": 1687116861.585662
  },
  "18311": {
    "problemId": "18311",
    "problemLevel": 6,
    "problemName": "왕복",
    "average_try": 3.0818,
    "solvedtags": [
      {
        "bojTagId": 102,
        "key": "implementation"
      }
    ],
    "lastupdate": 1687116861.585698
  },
  "1244": {
    "problemId": "1244",
    "problemLevel": 7,
    "problemName": "스위치 켜고 끄기",
    "average_try": 5.0405,
    "solvedtags": [
      {
        "bojTagId": 102,
        "key": "implementation"
      },
      {
        "bojTagId": 141,
        "key": "simulation"
      }
    ],
    "lastupdate": 1687116861.585717
  },
  "10994": {
    "problemId": "10994",
    "problemLevel": 7,
    "problemName": "별 찍기 - 19",
    "average_try": 1.482,
    "solvedtags": [
      {
        "bojTagId": 102,
        "key": "implementation"
      },
      {
        "bojTagId": 62,
        "key": "recursion"
      }
    ],
    "lastupdate": 1687116861.585735
  },
  "5766": {
    "problemId": "5766",
    "problemLevel": 7,
    "problemName": "할아버지는 유명해!",
    "average_try": 1.7921,
    "solvedtags": [
      {
        "bojTagId": 102,
        "key": "implementation"
      }
    ],
    "lastupdate": 1687116861.585764
  },
  "2615": {
    "problemId": "2615",
    "problemLevel": 10,
    "problemName": "오목",
    "average_try": 5.1566,
    "solvedtags": [
      {
        "bojTagId": 125,
        "key": "bruteforcing"
      },
      {
        "bojTagId": 102,
        "key": "implementation"
      }
    ],
    "lastupdate": 1687116861.585837
  },
  "2729": {
    "problemId": "2729",
    "problemLevel": 5,
    "problemName": "이진수 덧셈",
    "average_try": 2.3438,
    "solvedtags": [
      {
        "bojTagId": 121,
        "key": "arithmetic"
      },
      {
        "bojTagId": 102,
        "key": "implementation"
      },
      {
        "bojTagId": 124,
        "key": "math"
      }
    ],
    "lastupdate": 1687116861.585854
  },
  "17276": {
    "problemId": "17276",
    "problemLevel": 9,
    "problemName": "배열 돌리기",
    "average_try": 1.7729,
    "solvedtags": [
      {
        "bojTagId": 102,
        "key": "implementation"
      }
    ],
    "lastupdate": 1687116861.585872
  },
  "16926": {
    "problemId": "16926",
    "problemLevel": 10,
    "problemName": "배열 돌리기 1",
    "average_try": 2.1459,
    "solvedtags": [
      {
        "bojTagId": 102,
        "key": "implementation"
      }
    ],
    "lastupdate": 1687116861.58589
  },
  "16927": {
    "problemId": "16927",
    "problemLevel": 11,
    "problemName": "배열 돌리기 2",
    "average_try": 2.8835,
    "solvedtags": [
      {
        "bojTagId": 102,
        "key": "implementation"
      }
    ],
    "lastupdate": 1687116861.585908
  },
  "16935": {
    "problemId": "16935",
    "problemLevel": 10,
    "problemName": "배열 돌리기 3",
    "average_try": 1.9665,
    "solvedtags": [
      {
        "bojTagId": 102,
        "key": "implementation"
      }
    ],
    "lastupdate": 1687116861.585926
  },
  "17406": {
    "problemId": "17406",
    "problemLevel": 12,
    "problemName": "배열 돌리기 4",
    "average_try": 2.5581,
    "solvedtags": [
      {
        "bojTagId": 5,
        "key": "backtracking"
      },
      {
        "bojTagId": 125,
        "key": "bruteforcing"
      },
      {
        "bojTagId": 102,
        "key": "implementation"
      }
    ],
    "lastupdate": 1687116861.585943
  },
  "17470": {
    "problemId": "17470",
    "problemLevel": 16,
    "problemName": "배열 돌리기 5",
    "average_try": 4.6667,
    "solvedtags": [
      {
        "bojTagId": 102,
        "key": "implementation"
      }
    ],
    "lastupdate": 1687116861.58596
  },
  "20327": {
    "problemId": "20327",
    "problemLevel": 13,
    "problemName": "배열 돌리기 6",
    "average_try": 1.7254,
    "solvedtags": [
      {
        "bojTagId": 102,
        "key": "implementation"
      },
      {
        "bojTagId": 141,
        "key": "simulation"
      }
    ],
    "lastupdate": 1687116861.585977
  },
  "17128": {
    "problemId": "17128",
    "problemLevel": 9,
    "problemName": "소가 정보섬에 올라온 이유",
    "average_try": 2.1346,
    "solvedtags": [
      {
        "bojTagId": 102,
        "key": "implementation"
      },
      {
        "bojTagId": 124,
        "key": "math"
      }
    ],
    "lastupdate": 1687116861.585994
  },
  "1283": {
    "problemId": "1283",
    "problemLevel": 9,
    "problemName": "단축키 지정",
    "average_try": 2.6968,
    "solvedtags": [
      {
        "bojTagId": 102,
        "key": "implementation"
      },
      {
        "bojTagId": 158,
        "key": "string"
      }
    ],
    "lastupdate": 1687116861.586012
  },
  "10703": {
    "problemId": "10703",
    "problemLevel": 10,
    "problemName": "유성",
    "average_try": 4.3097,
    "solvedtags": [
      {
        "bojTagId": 102,
        "key": "implementation"
      }
    ],
    "lastupdate": 1687116861.586043
  },
  "2469": {
    "problemId": "2469",
    "problemLevel": 11,
    "problemName": "사다리 타기",
    "average_try": 2.5802,
    "solvedtags": [
      {
        "bojTagId": 102,
        "key": "implementation"
      },
      {
        "bojTagId": 158,
        "key": "string"
      }
    ],
    "lastupdate": 1687116861.58608
  },
  "2877": {
    "problemId": "2877",
    "problemLevel": 11,
    "problemName": "4와 7",
    "average_try": 1.6644,
    "solvedtags": [
      {
        "bojTagId": 102,
        "key": "implementation"
      },
      {
        "bojTagId": 124,
        "key": "math"
      }
    ],
    "lastupdate": 1687116861.586097
  },
  "15787": {
    "problemId": "15787",
    "problemLevel": 9,
    "problemName": "기차가 어둠을 헤치고 은하수를",
    "average_try": 3.4647,
    "solvedtags": [
      {
        "bojTagId": 14,
        "key": "bitmask"
      },
      {
        "bojTagId": 102,
        "key": "implementation"
      }
    ],
    "lastupdate": 1687116861.586115
  },
  "20164": {
    "problemId": "20164",
    "problemLevel": 11,
    "problemName": "홀수 홀릭 호석",
    "average_try": 1.4459,
    "solvedtags": [
      {
        "bojTagId": 125,
        "key": "bruteforcing"
      },
      {
        "bojTagId": 102,
        "key": "implementation"
      },
      {
        "bojTagId": 62,
        "key": "recursion"
      }
    ],
    "lastupdate": 1687116861.586133
  },
  "20207": {
    "problemId": "20207",
    "problemLevel": 11,
    "problemName": "달력",
    "average_try": 2.2894,
    "solvedtags": [
      {
        "bojTagId": 33,
        "key": "greedy"
      },
      {
        "bojTagId": 102,
        "key": "implementation"
      },
      {
        "bojTagId": 97,
        "key": "sorting"
      }
    ],
    "lastupdate": 1687116861.58615
  },
  "14719": {
    "problemId": "14719",
    "problemLevel": 11,
    "problemName": "빗물",
    "average_try": 1.7918,
    "solvedtags": [
      {
        "bojTagId": 102,
        "key": "implementation"
      },
      {
        "bojTagId": 141,
        "key": "simulation"
      }
    ],
    "lastupdate": 1687116861.586169
  },
  "15886": {
    "problemId": "15886",
    "problemLevel": 8,
    "problemName": "내 선물을 받아줘 2",
    "average_try": 1.4953,
    "solvedtags": [
      {
        "bojTagId": 7,
        "key": "graphs"
      },
      {
        "bojTagId": 158,
        "key": "string"
      }
    ],
    "lastupdate": 1687116861.586187
  },
  "16719": {
    "problemId": "16719",
    "problemLevel": 11,
    "problemName": "ZOAC",
    "average_try": 1.8692,
    "solvedtags": [
      {
        "bojTagId": 102,
        "key": "implementation"
      },
      {
        "bojTagId": 62,
        "key": "recursion"
      },
      {
        "bojTagId": 158,
        "key": "string"
      }
    ],
    "lastupdate": 1687116861.586204
  },
  "1022": {
    "problemId": "1022",
    "problemLevel": 13,
    "problemName": "소용돌이 예쁘게 출력하기",
    "average_try": 3.391,
    "solvedtags": [
      {
        "bojTagId": 102,
        "key": "implementation"
      },
      {
        "bojTagId": 124,
        "key": "math"
      }
    ],
    "lastupdate": 1687116861.586222
  },
  "9081": {
    "problemId": "9081",
    "problemLevel": 10,
    "problemName": "단어 맞추기",
    "average_try": 2.1596,
    "solvedtags": [
      {
        "bojTagId": 6,
        "key": "combinatorics"
      },
      {
        "bojTagId": 102,
        "key": "implementation"
      },
      {
        "bojTagId": 124,
        "key": "math"
      },
      {
        "bojTagId": 158,
        "key": "string"
      }
    ],
    "lastupdate": 1687116861.586239
  },
  "15806": {
    "problemId": "15806",
    "problemLevel": 16,
    "problemName": "영우의 기숙사 청소",
    "average_try": 5.6517,
    "solvedtags": [
      {
        "bojTagId": 126,
        "key": "bfs"
      },
      {
        "bojTagId": 7,
        "key": "graphs"
      },
      {
        "bojTagId": 11,
        "key": "graph_traversal"
      }
    ],
    "lastupdate": 1687116861.586257
  },
  "21277": {
    "problemId": "21277",
    "problemLevel": 13,
    "problemName": "짠돌이 호석",
    "average_try": 4.4098,
    "solvedtags": [
      {
        "bojTagId": 125,
        "key": "bruteforcing"
      },
      {
        "bojTagId": 102,
        "key": "implementation"
      }
    ],
    "lastupdate": 1687116861.586275
  },
  "21611": {
    "problemId": "21611",
    "problemLevel": 15,
    "problemName": "마법사 상어와 블리자드",
    "average_try": 4.2,
    "solvedtags": [
      {
        "bojTagId": 102,
        "key": "implementation"
      },
      {
        "bojTagId": 141,
        "key": "simulation"
      }
    ],
    "lastupdate": 1687116861.586293
  },
  "21608": {
    "problemId": "21608",
    "problemLevel": 11,
    "problemName": "상어 초등학교",
    "average_try": 2.4737,
    "solvedtags": [
      {
        "bojTagId": 102,
        "key": "implementation"
      }
    ],
    "lastupdate": 1687116861.586311
  },
  "21756": {
    "problemId": "21756",
    "problemLevel": 4,
    "problemName": "지우개",
    "average_try": 1.7459,
    "solvedtags": [
      {
        "bojTagId": 102,
        "key": "implementation"
      },
      {
        "bojTagId": 124,
        "key": "math"
      },
      {
        "bojTagId": 141,
        "key": "simulation"
      }
    ],
    "lastupdate": 1687116861.586328
  },
  "21918": {
    "problemId": "21918",
    "problemLevel": 4,
    "problemName": "전구",
    "average_try": 1.7059,
    "solvedtags": [
      {
        "bojTagId": 102,
        "key": "implementation"
      },
      {
        "bojTagId": 141,
        "key": "simulation"
      }
    ],
    "lastupdate": 1687116861.586346
  },
  "22860": {
    "problemId": "22860",
    "problemLevel": 13,
    "problemName": "폴더 정리 (small)",
    "average_try": 2.5921,
    "solvedtags": [
      {
        "bojTagId": 175,
        "key": "data_structures"
      },
      {
        "bojTagId": 127,
        "key": "dfs"
      },
      {
        "bojTagId": 7,
        "key": "graphs"
      },
      {
        "bojTagId": 11,
        "key": "graph_traversal"
      },
      {
        "bojTagId": 136,
        "key": "hash_set"
      },
      {
        "bojTagId": 120,
        "key": "trees"
      }
    ],
    "lastupdate": 1687116861.586363
  },
  "22859": {
    "problemId": "22859",
    "problemLevel": 13,
    "problemName": "HTML 파싱",
    "average_try": 4.7161,
    "solvedtags": [
      {
        "bojTagId": 102,
        "key": "implementation"
      },
      {
        "bojTagId": 96,
        "key": "parsing"
      },
      {
        "bojTagId": 63,
        "key": "regex"
      },
      {
        "bojTagId": 158,
        "key": "string"
      }
    ],
    "lastupdate": 1687116861.586382
  },
  "22856": {
    "problemId": "22856",
    "problemLevel": 12,
    "problemName": "트리 순회",
    "average_try": 3.3684,
    "solvedtags": [
      {
        "bojTagId": 7,
        "key": "graphs"
      },
      {
        "bojTagId": 11,
        "key": "graph_traversal"
      },
      {
        "bojTagId": 120,
        "key": "trees"
      }
    ],
    "lastupdate": 1687116861.586399
  },
  "22858": {
    "problemId": "22858",
    "problemLevel": 8,
    "problemName": "원상 복구 (small)",
    "average_try": 1.6401,
    "solvedtags": [
      {
        "bojTagId": 102,
        "key": "implementation"
      },
      {
        "bojTagId": 141,
        "key": "simulation"
      }
    ],
    "lastupdate": 1687116861.586417
  },
  "1978": {
    "problemId": "1978",
    "problemLevel": 4,
    "problemName": "소수 찾기",
    "average_try": 2.139,
    "solvedtags": [
      {
        "bojTagId": 9,
        "key": "primality_test"
      },
      {
        "bojTagId": 95,
        "key": "number_theory"
      },
      {
        "bojTagId": 124,
        "key": "math"
      }
    ],
    "lastupdate": 1687116861.586989
  },
  "2609": {
    "problemId": "2609",
    "problemLevel": 5,
    "problemName": "최대공약수와 최소공배수",
    "average_try": 1.7267,
    "solvedtags": [
      {
        "bojTagId": 26,
        "key": "euclidean"
      },
      {
        "bojTagId": 124,
        "key": "math"
      },
      {
        "bojTagId": 95,
        "key": "number_theory"
      }
    ],
    "lastupdate": 1687116861.587014
  },
  "1934": {
    "problemId": "1934",
    "problemLevel": 5,
    "problemName": "최소공배수",
    "average_try": 1.7557,
    "solvedtags": [
      {
        "bojTagId": 26,
        "key": "euclidean"
      },
      {
        "bojTagId": 124,
        "key": "math"
      },
      {
        "bojTagId": 95,
        "key": "number_theory"
      }
    ],
    "lastupdate": 1687116861.587033
  },
  "2581": {
    "problemId": "2581",
    "problemLevel": 4,
    "problemName": "소수",
    "average_try": 2.5541,
    "solvedtags": [
      {
        "bojTagId": 9,
        "key": "primality_test"
      },
      {
        "bojTagId": 95,
        "key": "number_theory"
      },
      {
        "bojTagId": 124,
        "key": "math"
      }
    ],
    "lastupdate": 1687116861.587202
  },
  "11653": {
    "problemId": "11653",
    "problemLevel": 5,
    "problemName": "소인수분해",
    "average_try": 1.8941,
    "solvedtags": [
      {
        "bojTagId": 124,
        "key": "math"
      },
      {
        "bojTagId": 95,
        "key": "number_theory"
      },
      {
        "bojTagId": 9,
        "key": "primality_test"
      }
    ],
    "lastupdate": 1687116861.587221
  },
  "2960": {
    "problemId": "2960",
    "problemLevel": 7,
    "problemName": "에라토스테네스의 체",
    "average_try": 1.779,
    "solvedtags": [
      {
        "bojTagId": 102,
        "key": "implementation"
      },
      {
        "bojTagId": 124,
        "key": "math"
      },
      {
        "bojTagId": 95,
        "key": "number_theory"
      },
      {
        "bojTagId": 9,
        "key": "primality_test"
      },
      {
        "bojTagId": 67,
        "key": "sieve"
      }
    ],
    "lastupdate": 1687116861.58724
  },
  "9613": {
    "problemId": "9613",
    "problemLevel": 7,
    "problemName": "GCD 합",
    "average_try": 2.4272,
    "solvedtags": [
      {
        "bojTagId": 26,
        "key": "euclidean"
      },
      {
        "bojTagId": 124,
        "key": "math"
      },
      {
        "bojTagId": 95,
        "key": "number_theory"
      }
    ],
    "lastupdate": 1687116861.587259
  },
  "5347": {
    "problemId": "5347",
    "problemLevel": 6,
    "problemName": "LCM",
    "average_try": 1.9404,
    "solvedtags": [
      {
        "bojTagId": 26,
        "key": "euclidean"
      },
      {
        "bojTagId": 124,
        "key": "math"
      },
      {
        "bojTagId": 95,
        "key": "number_theory"
      }
    ],
    "lastupdate": 1687116861.587277
  },
  "4134": {
    "problemId": "4134",
    "problemLevel": 7,
    "problemName": "다음 소수",
    "average_try": 3.9014,
    "solvedtags": [
      {
        "bojTagId": 125,
        "key": "bruteforcing"
      },
      {
        "bojTagId": 124,
        "key": "math"
      },
      {
        "bojTagId": 95,
        "key": "number_theory"
      },
      {
        "bojTagId": 9,
        "key": "primality_test"
      }
    ],
    "lastupdate": 1687116861.587307
  },
  "1110": {
    "problemId": "1110",
    "problemLevel": 5,
    "problemName": "더하기 사이클",
    "average_try": 2.1426,
    "solvedtags": [
      {
        "bojTagId": 102,
        "key": "implementation"
      },
      {
        "bojTagId": 124,
        "key": "math"
      }
    ],
    "lastupdate": 1687116861.587325
  },
  "5618": {
    "problemId": "5618",
    "problemLevel": 4,
    "problemName": "공약수",
    "average_try": 1.9489,
    "solvedtags": [
      {
        "bojTagId": 125,
        "key": "bruteforcing"
      },
      {
        "bojTagId": 124,
        "key": "math"
      },
      {
        "bojTagId": 95,
        "key": "number_theory"
      }
    ],
    "lastupdate": 1687116861.587343
  },
  "2745": {
    "problemId": "2745",
    "problemLevel": 4,
    "problemName": "진법 변환",
    "average_try": 1.8656,
    "solvedtags": [
      {
        "bojTagId": 102,
        "key": "implementation"
      },
      {
        "bojTagId": 158,
        "key": "string"
      },
      {
        "bojTagId": 124,
        "key": "math"
      }
    ],
    "lastupdate": 1687116861.587361
  },
  "21275": {
    "problemId": "21275",
    "problemLevel": 9,
    "problemName": "폰 호석만",
    "average_try": 2.5793,
    "solvedtags": [
      {
        "bojTagId": 125,
        "key": "bruteforcing"
      },
      {
        "bojTagId": 124,
        "key": "math"
      }
    ],
    "lastupdate": 1687116861.587378
  },
  "1456": {
    "problemId": "1456",
    "problemLevel": 11,
    "problemName": "거의 소수",
    "average_try": 4.1554,
    "solvedtags": [
      {
        "bojTagId": 124,
        "key": "math"
      },
      {
        "bojTagId": 95,
        "key": "number_theory"
      },
      {
        "bojTagId": 9,
        "key": "primality_test"
      },
      {
        "bojTagId": 67,
        "key": "sieve"
      }
    ],
    "lastupdate": 1687116861.587396
  },
  "2168": {
    "problemId": "2168",
    "problemLevel": 10,
    "problemName": "타일 위의 대각선",
    "average_try": 1.8088,
    "solvedtags": [
      {
        "bojTagId": 26,
        "key": "euclidean"
      },
      {
        "bojTagId": 124,
        "key": "math"
      },
      {
        "bojTagId": 95,
        "key": "number_theory"
      }
    ],
    "lastupdate": 1687116861.587414
  },
  "9421": {
    "problemId": "9421",
    "problemLevel": 10,
    "problemName": "소수상근수",
    "average_try": 1.9061,
    "solvedtags": [
      {
        "bojTagId": 124,
        "key": "math"
      },
      {
        "bojTagId": 95,
        "key": "number_theory"
      },
      {
        "bojTagId": 9,
        "key": "primality_test"
      },
      {
        "bojTagId": 67,
        "key": "sieve"
      }
    ],
    "lastupdate": 1687116861.587432
  },
  "1669": {
    "problemId": "1669",
    "problemLevel": 11,
    "problemName": "멍멍이 쓰다듬기",
    "average_try": 2.7046,
    "solvedtags": [
      {
        "bojTagId": 124,
        "key": "math"
      }
    ],
    "lastupdate": 1687116861.58745
  },
  "1990": {
    "problemId": "1990",
    "problemLevel": 11,
    "problemName": "소수인팰린드롬",
    "average_try": 4.3965,
    "solvedtags": [
      {
        "bojTagId": 124,
        "key": "math"
      },
      {
        "bojTagId": 95,
        "key": "number_theory"
      },
      {
        "bojTagId": 9,
        "key": "primality_test"
      },
      {
        "bojTagId": 67,
        "key": "sieve"
      }
    ],
    "lastupdate": 1687116861.587468
  },
  "3343": {
    "problemId": "3343",
    "problemLevel": 12,
    "problemName": "장미",
    "average_try": 6.0121,
    "solvedtags": [
      {
        "bojTagId": 125,
        "key": "bruteforcing"
      },
      {
        "bojTagId": 124,
        "key": "math"
      },
      {
        "bojTagId": 95,
        "key": "number_theory"
      }
    ],
    "lastupdate": 1687116861.587486
  },
  "1747": {
    "problemId": "1747",
    "problemLevel": 10,
    "problemName": "소수&팰린드롬",
    "average_try": 3.2869,
    "solvedtags": [
      {
        "bojTagId": 125,
        "key": "bruteforcing"
      },
      {
        "bojTagId": 124,
        "key": "math"
      },
      {
        "bojTagId": 95,
        "key": "number_theory"
      },
      {
        "bojTagId": 9,
        "key": "primality_test"
      },
      {
        "bojTagId": 67,
        "key": "sieve"
      }
    ],
    "lastupdate": 1687116861.587503
  },
  "2436": {
    "problemId": "2436",
    "problemLevel": 11,
    "problemName": "공약수",
    "average_try": 3.2394,
    "solvedtags": [
      {
        "bojTagId": 125,
        "key": "bruteforcing"
      },
      {
        "bojTagId": 26,
        "key": "euclidean"
      },
      {
        "bojTagId": 124,
        "key": "math"
      },
      {
        "bojTagId": 95,
        "key": "number_theory"
      }
    ],
    "lastupdate": 1687116861.58752
  },
  "1188": {
    "problemId": "1188",
    "problemLevel": 12,
    "problemName": "음식 평론가",
    "average_try": 2.0695,
    "solvedtags": [
      {
        "bojTagId": 26,
        "key": "euclidean"
      },
      {
        "bojTagId": 124,
        "key": "math"
      },
      {
        "bojTagId": 95,
        "key": "number_theory"
      }
    ],
    "lastupdate": 1687116861.587537
  },
  "2824": {
    "problemId": "2824",
    "problemLevel": 10,
    "problemName": "최대공약수",
    "average_try": 3.7031,
    "solvedtags": [
      {
        "bojTagId": 102,
        "key": "implementation"
      },
      {
        "bojTagId": 124,
        "key": "math"
      },
      {
        "bojTagId": 95,
        "key": "number_theory"
      },
      {
        "bojTagId": 9,
        "key": "primality_test"
      }
    ],
    "lastupdate": 1687116861.587554
  },
  "2553": {
    "problemId": "2553",
    "problemLevel": 9,
    "problemName": "마지막 팩토리얼 수",
    "average_try": 3.1125,
    "solvedtags": [
      {
        "bojTagId": 124,
        "key": "math"
      },
      {
        "bojTagId": 95,
        "key": "number_theory"
      }
    ],
    "lastupdate": 1687116861.587571
  },
  "21312": {
    "problemId": "21312",
    "problemLevel": 3,
    "problemName": "홀짝 칵테일",
    "average_try": 1.6219,
    "solvedtags": [
      {
        "bojTagId": 121,
        "key": "arithmetic"
      },
      {
        "bojTagId": 102,
        "key": "implementation"
      },
      {
        "bojTagId": 124,
        "key": "math"
      }
    ],
    "lastupdate": 1687116861.587589
  },
  "21920": {
    "problemId": "21920",
    "problemLevel": 7,
    "problemName": "서로소 평균",
    "average_try": 2.6148,
    "solvedtags": [
      {
        "bojTagId": 26,
        "key": "euclidean"
      },
      {
        "bojTagId": 124,
        "key": "math"
      },
      {
        "bojTagId": 95,
        "key": "number_theory"
      }
    ],
    "lastupdate": 1687116861.587606
  },
  "21919": {
    "problemId": "21919",
    "problemLevel": 8,
    "problemName": "소수 최소 공배수",
    "average_try": 3.7458,
    "solvedtags": [
      {
        "bojTagId": 124,
        "key": "math"
      },
      {
        "bojTagId": 95,
        "key": "number_theory"
      },
      {
        "bojTagId": 9,
        "key": "primality_test"
      },
      {
        "bojTagId": 67,
        "key": "sieve"
      }
    ],
    "lastupdate": 1687116861.587624
  },
  "22864": {
    "problemId": "22864",
    "problemLevel": 4,
    "problemName": "피로도",
    "average_try": 2.2277,
    "solvedtags": [
      {
        "bojTagId": 121,
        "key": "arithmetic"
      },
      {
        "bojTagId": 33,
        "key": "greedy"
      },
      {
        "bojTagId": 102,
        "key": "implementation"
      },
      {
        "bojTagId": 124,
        "key": "math"
      },
      {
        "bojTagId": 141,
        "key": "simulation"
      }
    ],
    "lastupdate": 1687116861.587641
  },
  "22943": {
    "problemId": "22943",
    "problemLevel": 11,
    "problemName": "수",
    "average_try": 5.6404,
    "solvedtags": [
      {
        "bojTagId": 125,
        "key": "bruteforcing"
      },
      {
        "bojTagId": 102,
        "key": "implementation"
      },
      {
        "bojTagId": 124,
        "key": "math"
      },
      {
        "bojTagId": 95,
        "key": "number_theory"
      },
      {
        "bojTagId": 9,
        "key": "primality_test"
      },
      {
        "bojTagId": 67,
        "key": "sieve"
      }
    ],
    "lastupdate": 1687116861.587659
  },
  "1197": {
    "problemId": "1197",
    "problemLevel": 12,
    "problemName": "최소 스패닝 트리",
    "average_try": 2.4461,
    "solvedtags": [
      {
        "bojTagId": 49,
        "key": "mst"
      },
      {
        "bojTagId": 7,
        "key": "graphs"
      }
    ],
    "lastupdate": 1687116861.588069
  },
  "1922": {
    "problemId": "1922",
    "problemLevel": 12,
    "problemName": "네트워크 연결",
    "average_try": 1.5888,
    "solvedtags": [
      {
        "bojTagId": 7,
        "key": "graphs"
      },
      {
        "bojTagId": 49,
        "key": "mst"
      }
    ],
    "lastupdate": 1687116861.588092
  },
  "1647": {
    "problemId": "1647",
    "problemLevel": 12,
    "problemName": "도시 분할 계획",
    "average_try": 2.0134,
    "solvedtags": [
      {
        "bojTagId": 7,
        "key": "graphs"
      },
      {
        "bojTagId": 49,
        "key": "mst"
      }
    ],
    "lastupdate": 1687116861.588112
  },
  "4386": {
    "problemId": "4386",
    "problemLevel": 13,
    "problemName": "별자리 만들기",
    "average_try": 1.7198,
    "solvedtags": [
      {
        "bojTagId": 7,
        "key": "graphs"
      },
      {
        "bojTagId": 49,
        "key": "mst"
      }
    ],
    "lastupdate": 1687116861.588131
  },
  "6497": {
    "problemId": "6497",
    "problemLevel": 12,
    "problemName": "전력난",
    "average_try": 2.9302,
    "solvedtags": [
      {
        "bojTagId": 7,
        "key": "graphs"
      },
      {
        "bojTagId": 49,
        "key": "mst"
      }
    ],
    "lastupdate": 1687116861.58815
  },
  "1774": {
    "problemId": "1774",
    "problemLevel": 13,
    "problemName": "우주신과의 교감",
    "average_try": 3.3422,
    "solvedtags": [
      {
        "bojTagId": 7,
        "key": "graphs"
      },
      {
        "bojTagId": 49,
        "key": "mst"
      }
    ],
    "lastupdate": 1687116861.588182
  },
  "16398": {
    "problemId": "16398",
    "problemLevel": 12,
    "problemName": "행성 연결",
    "average_try": 2.3022,
    "solvedtags": [
      {
        "bojTagId": 7,
        "key": "graphs"
      },
      {
        "bojTagId": 49,
        "key": "mst"
      }
    ],
    "lastupdate": 1687116861.5882
  },
  "13905": {
    "problemId": "13905",
    "problemLevel": 12,
    "problemName": "세부",
    "average_try": 3.2168,
    "solvedtags": [
      {
        "bojTagId": 175,
        "key": "data_structures"
      },
      {
        "bojTagId": 81,
        "key": "disjoint_set"
      },
      {
        "bojTagId": 7,
        "key": "graphs"
      },
      {
        "bojTagId": 11,
        "key": "graph_traversal"
      },
      {
        "bojTagId": 49,
        "key": "mst"
      }
    ],
    "lastupdate": 1687116861.588218
  },
  "16202": {
    "problemId": "16202",
    "problemLevel": 12,
    "problemName": "MST 게임",
    "average_try": 1.5399,
    "solvedtags": [
      {
        "bojTagId": 7,
        "key": "graphs"
      },
      {
        "bojTagId": 49,
        "key": "mst"
      }
    ],
    "lastupdate": 1687116861.588236
  },
  "18769": {
    "problemId": "18769",
    "problemLevel": 12,
    "problemName": "그리드 네트워크",
    "average_try": 2.6822,
    "solvedtags": [
      {
        "bojTagId": 7,
        "key": "graphs"
      },
      {
        "bojTagId": 49,
        "key": "mst"
      }
    ],
    "lastupdate": 1687116861.588254
  },
  "17472": {
    "problemId": "17472",
    "problemLevel": 15,
    "problemName": "다리 만들기 2",
    "average_try": 3.0766,
    "solvedtags": [
      {
        "bojTagId": 126,
        "key": "bfs"
      },
      {
        "bojTagId": 125,
        "key": "bruteforcing"
      },
      {
        "bojTagId": 127,
        "key": "dfs"
      },
      {
        "bojTagId": 7,
        "key": "graphs"
      },
      {
        "bojTagId": 11,
        "key": "graph_traversal"
      },
      {
        "bojTagId": 102,
        "key": "implementation"
      },
      {
        "bojTagId": 49,
        "key": "mst"
      }
    ],
    "lastupdate": 1687116861.588273
  },
  "13418": {
    "problemId": "13418",
    "problemLevel": 13,
    "problemName": "학교 탐방하기",
    "average_try": 2.6214,
    "solvedtags": [
      {
        "bojTagId": 7,
        "key": "graphs"
      },
      {
        "bojTagId": 49,
        "key": "mst"
      }
    ],
    "lastupdate": 1687116861.588291
  },
  "14621": {
    "problemId": "14621",
    "problemLevel": 13,
    "problemName": "나만 안되는 연애",
    "average_try": 2.095,
    "solvedtags": [
      {
        "bojTagId": 7,
        "key": "graphs"
      },
      {
        "bojTagId": 49,
        "key": "mst"
      }
    ],
    "lastupdate": 1687116861.588308
  },
  "14950": {
    "problemId": "14950",
    "problemLevel": 13,
    "problemName": "정복자",
    "average_try": 1.784,
    "solvedtags": [
      {
        "bojTagId": 7,
        "key": "graphs"
      },
      {
        "bojTagId": 49,
        "key": "mst"
      }
    ],
    "lastupdate": 1687116861.588325
  },
  "2406": {
    "problemId": "2406",
    "problemLevel": 13,
    "problemName": "안정적인 네트워크",
    "average_try": 2.6048,
    "solvedtags": [
      {
        "bojTagId": 7,
        "key": "graphs"
      },
      {
        "bojTagId": 49,
        "key": "mst"
      }
    ],
    "lastupdate": 1687116861.588342
  },
  "17490": {
    "problemId": "17490",
    "problemLevel": 13,
    "problemName": "일감호에 다리 놓기",
    "average_try": 4.886,
    "solvedtags": [
      {
        "bojTagId": 175,
        "key": "data_structures"
      },
      {
        "bojTagId": 81,
        "key": "disjoint_set"
      },
      {
        "bojTagId": 7,
        "key": "graphs"
      },
      {
        "bojTagId": 33,
        "key": "greedy"
      },
      {
        "bojTagId": 49,
        "key": "mst"
      }
    ],
    "lastupdate": 1687116861.58836
  },
  "2887": {
    "problemId": "2887",
    "problemLevel": 16,
    "problemName": "행성 터널",
    "average_try": 2.866,
    "solvedtags": [
      {
        "bojTagId": 7,
        "key": "graphs"
      },
      {
        "bojTagId": 49,
        "key": "mst"
      },
      {
        "bojTagId": 97,
        "key": "sorting"
      }
    ],
    "lastupdate": 1687116861.588378
  },
  "1944": {
    "problemId": "1944",
    "problemLevel": 15,
    "problemName": "복제 로봇",
    "average_try": 3.8317,
    "solvedtags": [
      {
        "bojTagId": 126,
        "key": "bfs"
      },
      {
        "bojTagId": 7,
        "key": "graphs"
      },
      {
        "bojTagId": 11,
        "key": "graph_traversal"
      },
      {
        "bojTagId": 49,
        "key": "mst"
      }
    ],
    "lastupdate": 1687116861.588395
  },
  "10423": {
    "problemId": "10423",
    "problemLevel": 14,
    "problemName": "전기가 부족해",
    "average_try": 1.4286,
    "solvedtags": [
      {
        "bojTagId": 7,
        "key": "graphs"
      },
      {
        "bojTagId": 49,
        "key": "mst"
      }
    ],
    "lastupdate": 1687116861.588413
  },
  "1368": {
    "problemId": "1368",
    "problemLevel": 14,
    "problemName": "물대기",
    "average_try": 2.3434,
    "solvedtags": [
      {
        "bojTagId": 7,
        "key": "graphs"
      },
      {
        "bojTagId": 49,
        "key": "mst"
      }
    ],
    "lastupdate": 1687116861.58843
  },
  "20010": {
    "problemId": "20010",
    "problemLevel": 14,
    "problemName": "악덕 영주 혜유",
    "average_try": 1.7676,
    "solvedtags": [
      {
        "bojTagId": 127,
        "key": "dfs"
      },
      {
        "bojTagId": 7,
        "key": "graphs"
      },
      {
        "bojTagId": 11,
        "key": "graph_traversal"
      },
      {
        "bojTagId": 49,
        "key": "mst"
      }
    ],
    "lastupdate": 1687116861.588448
  },
  "1414": {
    "problemId": "1414",
    "problemLevel": 13,
    "problemName": "불우이웃돕기",
    "average_try": 2.3482,
    "solvedtags": [
      {
        "bojTagId": 7,
        "key": "graphs"
      },
      {
        "bojTagId": 49,
        "key": "mst"
      },
      {
        "bojTagId": 158,
        "key": "string"
      }
    ],
    "lastupdate": 1687116861.588466
  },
  "1045": {
    "problemId": "1045",
    "problemLevel": 15,
    "problemName": "도로",
    "average_try": 3.68,
    "solvedtags": [
      {
        "bojTagId": 7,
        "key": "graphs"
      },
      {
        "bojTagId": 33,
        "key": "greedy"
      },
      {
        "bojTagId": 49,
        "key": "mst"
      }
    ],
    "lastupdate": 1687116861.588483
  },
  "21924": {
    "problemId": "21924",
    "problemLevel": 12,
    "problemName": "도시 건설",
    "average_try": 2.3309,
    "solvedtags": [
      {
        "bojTagId": 7,
        "key": "graphs"
      },
      {
        "bojTagId": 49,
        "key": "mst"
      }
    ],
    "lastupdate": 1687116861.588501
  },
  "14929": {
    "problemId": "14929",
    "problemLevel": 6,
    "problemName": "귀찮아 (SIB)",
    "average_try": 2.3063,
    "solvedtags": [
      {
        "bojTagId": 124,
        "key": "math"
      },
      {
        "bojTagId": 139,
        "key": "prefix_sum"
      }
    ],
    "lastupdate": 1687116861.588877
  },
  "2167": {
    "problemId": "2167",
    "problemLevel": 6,
    "problemName": "2차원 배열의 합",
    "average_try": 1.7397,
    "solvedtags": [
      {
        "bojTagId": 102,
        "key": "implementation"
      },
      {
        "bojTagId": 139,
        "key": "prefix_sum"
      }
    ],
    "lastupdate": 1687116861.588901
  },
  "20116": {
    "problemId": "20116",
    "problemLevel": 8,
    "problemName": "상자의 균형",
    "average_try": 2.8105,
    "solvedtags": [
      {
        "bojTagId": 124,
        "key": "math"
      },
      {
        "bojTagId": 116,
        "key": "physics"
      },
      {
        "bojTagId": 139,
        "key": "prefix_sum"
      }
    ],
    "lastupdate": 1687116861.588921
  },
  "11659": {
    "problemId": "11659",
    "problemLevel": 8,
    "problemName": "구간 합 구하기 4",
    "average_try": 2.5102,
    "solvedtags": [
      {
        "bojTagId": 139,
        "key": "prefix_sum"
      }
    ],
    "lastupdate": 1687116861.58894
  },
  "11441": {
    "problemId": "11441",
    "problemLevel": 8,
    "problemName": "합 구하기",
    "average_try": 1.9285,
    "solvedtags": [
      {
        "bojTagId": 139,
        "key": "prefix_sum"
      }
    ],
    "lastupdate": 1687116861.588958
  },
  "17390": {
    "problemId": "17390",
    "problemLevel": 8,
    "problemName": "이건 꼭 풀어야 해!",
    "average_try": 2.1215,
    "solvedtags": [
      {
        "bojTagId": 139,
        "key": "prefix_sum"
      },
      {
        "bojTagId": 97,
        "key": "sorting"
      }
    ],
    "lastupdate": 1687116861.588977
  },
  "16139": {
    "problemId": "16139",
    "problemLevel": 10,
    "problemName": "인간-컴퓨터 상호작용",
    "average_try": 3.4696,
    "solvedtags": [
      {
        "bojTagId": 139,
        "key": "prefix_sum"
      }
    ],
    "lastupdate": 1687116861.588995
  },
  "20438": {
    "problemId": "20438",
    "problemLevel": 9,
    "problemName": "출석체크",
    "average_try": 3.7583,
    "solvedtags": [
      {
        "bojTagId": 139,
        "key": "prefix_sum"
      }
    ],
    "lastupdate": 1687116861.589012
  },
  "17123": {
    "problemId": "17123",
    "problemLevel": 9,
    "problemName": "배열 놀이",
    "average_try": 1.9538,
    "solvedtags": [
      {
        "bojTagId": 139,
        "key": "prefix_sum"
      }
    ],
    "lastupdate": 1687116861.589043
  },
  "11660": {
    "problemId": "11660",
    "problemLevel": 10,
    "problemName": "구간 합 구하기 5",
    "average_try": 2.2184,
    "solvedtags": [
      {
        "bojTagId": 25,
        "key": "dp"
      },
      {
        "bojTagId": 139,
        "key": "prefix_sum"
      }
    ],
    "lastupdate": 1687116861.589061
  },
  "16507": {
    "problemId": "16507",
    "problemLevel": 10,
    "problemName": "어두운 건 무서워",
    "average_try": 1.5974,
    "solvedtags": [
      {
        "bojTagId": 139,
        "key": "prefix_sum"
      }
    ],
    "lastupdate": 1687116861.589078
  },
  "19951": {
    "problemId": "19951",
    "problemLevel": 11,
    "problemName": "태상이의 훈련소 생활",
    "average_try": 1.7615,
    "solvedtags": [
      {
        "bojTagId": 139,
        "key": "prefix_sum"
      }
    ],
    "lastupdate": 1687116861.589095
  },
  "10427": {
    "problemId": "10427",
    "problemLevel": 11,
    "problemName": "빚",
    "average_try": 1.7734,
    "solvedtags": [
      {
        "bojTagId": 33,
        "key": "greedy"
      },
      {
        "bojTagId": 139,
        "key": "prefix_sum"
      },
      {
        "bojTagId": 97,
        "key": "sorting"
      }
    ],
    "lastupdate": 1687116861.589113
  },
  "2015": {
    "problemId": "2015",
    "problemLevel": 12,
    "problemName": "수들의 합 4",
    "average_try": 2.8589,
    "solvedtags": [
      {
        "bojTagId": 175,
        "key": "data_structures"
      },
      {
        "bojTagId": 136,
        "key": "hash_set"
      },
      {
        "bojTagId": 139,
        "key": "prefix_sum"
      },
      {
        "bojTagId": 74,
        "key": "tree_set"
      }
    ],
    "lastupdate": 1687116861.589131
  },
  "10713": {
    "problemId": "10713",
    "problemLevel": 11,
    "problemName": "기차 여행",
    "average_try": 2.4308,
    "solvedtags": [
      {
        "bojTagId": 139,
        "key": "prefix_sum"
      }
    ],
    "lastupdate": 1687116861.589148
  },
  "20002": {
    "problemId": "20002",
    "problemLevel": 11,
    "problemName": "사과나무",
    "average_try": 1.8963,
    "solvedtags": [
      {
        "bojTagId": 125,
        "key": "bruteforcing"
      },
      {
        "bojTagId": 139,
        "key": "prefix_sum"
      }
    ],
    "lastupdate": 1687116861.589165
  },
  "20159": {
    "problemId": "20159",
    "problemLevel": 11,
    "problemName": "동작 그만. 밑장 빼기냐?",
    "average_try": 3.7112,
    "solvedtags": [
      {
        "bojTagId": 139,
        "key": "prefix_sum"
      }
    ],
    "lastupdate": 1687116861.589182
  },
  "18866": {
    "problemId": "18866",
    "problemLevel": 11,
    "problemName": "젊은 날의 생이여",
    "average_try": 4.0254,
    "solvedtags": [
      {
        "bojTagId": 139,
        "key": "prefix_sum"
      }
    ],
    "lastupdate": 1687116861.5892
  },
  "10986": {
    "problemId": "10986",
    "problemLevel": 13,
    "problemName": "나머지 합",
    "average_try": 3.651,
    "solvedtags": [
      {
        "bojTagId": 124,
        "key": "math"
      },
      {
        "bojTagId": 139,
        "key": "prefix_sum"
      }
    ],
    "lastupdate": 1687116861.589218
  },
  "5549": {
    "problemId": "5549",
    "problemLevel": 11,
    "problemName": "행성 탐사",
    "average_try": 2.1308,
    "solvedtags": [
      {
        "bojTagId": 139,
        "key": "prefix_sum"
      }
    ],
    "lastupdate": 1687116861.589236
  },
  "2571": {
    "problemId": "2571",
    "problemLevel": 13,
    "problemName": "색종이 - 3",
    "average_try": 1.9528,
    "solvedtags": [
      {
        "bojTagId": 102,
        "key": "implementation"
      },
      {
        "bojTagId": 139,
        "key": "prefix_sum"
      }
    ],
    "lastupdate": 1687116861.589254
  },
  "1749": {
    "problemId": "1749",
    "problemLevel": 12,
    "problemName": "점수따먹기",
    "average_try": 3.0625,
    "solvedtags": [
      {
        "bojTagId": 125,
        "key": "bruteforcing"
      },
      {
        "bojTagId": 25,
        "key": "dp"
      },
      {
        "bojTagId": 139,
        "key": "prefix_sum"
      }
    ],
    "lastupdate": 1687116861.589271
  },
  "20440": {
    "problemId": "20440",
    "problemLevel": 13,
    "problemName": "🎵니가 싫어 싫어 너무 싫어 싫어 오지 마 내게 찝쩍대지마🎵 - 1",
    "average_try": 2.9186,
    "solvedtags": [
      {
        "bojTagId": 161,
        "key": "coordinate_compression"
      },
      {
        "bojTagId": 139,
        "key": "prefix_sum"
      },
      {
        "bojTagId": 97,
        "key": "sorting"
      }
    ],
    "lastupdate": 1687116861.589288
  },
  "3673": {
    "problemId": "3673",
    "problemLevel": 13,
    "problemName": "나눌 수 있는 부분 수열",
    "average_try": 2.5494,
    "solvedtags": [
      {
        "bojTagId": 124,
        "key": "math"
      },
      {
        "bojTagId": 139,
        "key": "prefix_sum"
      }
    ],
    "lastupdate": 1687116861.589306
  },
  "5875": {
    "problemId": "5875",
    "problemLevel": 13,
    "problemName": "오타",
    "average_try": 2.5961,
    "solvedtags": [
      {
        "bojTagId": 175,
        "key": "data_structures"
      },
      {
        "bojTagId": 139,
        "key": "prefix_sum"
      }
    ],
    "lastupdate": 1687116861.589324
  },
  "14476": {
    "problemId": "14476",
    "problemLevel": 14,
    "problemName": "최대공약수 하나 빼기",
    "average_try": 1.9452,
    "solvedtags": [
      {
        "bojTagId": 26,
        "key": "euclidean"
      },
      {
        "bojTagId": 124,
        "key": "math"
      },
      {
        "bojTagId": 95,
        "key": "number_theory"
      },
      {
        "bojTagId": 139,
        "key": "prefix_sum"
      }
    ],
    "lastupdate": 1687116861.589342
  },
  "19566": {
    "problemId": "19566",
    "problemLevel": 14,
    "problemName": "수열의 구간 평균",
    "average_try": 2.0103,
    "solvedtags": [
      {
        "bojTagId": 175,
        "key": "data_structures"
      },
      {
        "bojTagId": 139,
        "key": "prefix_sum"
      },
      {
        "bojTagId": 74,
        "key": "tree_set"
      }
    ],
    "lastupdate": 1687116861.589359
  },
  "16971": {
    "problemId": "16971",
    "problemLevel": 13,
    "problemName": "배열 B의 값",
    "average_try": 2.8283,
    "solvedtags": [
      {
        "bojTagId": 33,
        "key": "greedy"
      },
      {
        "bojTagId": 124,
        "key": "math"
      },
      {
        "bojTagId": 139,
        "key": "prefix_sum"
      }
    ],
    "lastupdate": 1687116861.589377
  },
  "2900": {
    "problemId": "2900",
    "problemLevel": 13,
    "problemName": "프로그램",
    "average_try": 3.0443,
    "solvedtags": [
      {
        "bojTagId": 124,
        "key": "math"
      },
      {
        "bojTagId": 95,
        "key": "number_theory"
      },
      {
        "bojTagId": 139,
        "key": "prefix_sum"
      }
    ],
    "lastupdate": 1687116861.589394
  },
  "20543": {
    "problemId": "20543",
    "problemLevel": 15,
    "problemName": "폭탄 던지는 태영이",
    "average_try": 3.6205,
    "solvedtags": [
      {
        "bojTagId": 33,
        "key": "greedy"
      },
      {
        "bojTagId": 139,
        "key": "prefix_sum"
      }
    ],
    "lastupdate": 1687116861.589412
  },
  "21318": {
    "problemId": "21318",
    "problemLevel": 10,
    "problemName": "피아노 체조",
    "average_try": 2.1127,
    "solvedtags": [
      {
        "bojTagId": 139,
        "key": "prefix_sum"
      }
    ],
    "lastupdate": 1687116861.589429
  },
  "21757": {
    "problemId": "21757",
    "problemLevel": 14,
    "problemName": "나누기",
    "average_try": 4.8648,
    "solvedtags": [
      {
        "bojTagId": 25,
        "key": "dp"
      },
      {
        "bojTagId": 139,
        "key": "prefix_sum"
      }
    ],
    "lastupdate": 1687116861.589447
  },
  "18352": {
    "problemId": "18352",
    "problemLevel": 9,
    "problemName": "특정 거리의 도시 찾기",
    "average_try": 3.3576,
    "solvedtags": [
      {
        "bojTagId": 126,
        "key": "bfs"
      },
      {
        "bojTagId": 22,
        "key": "dijkstra"
      },
      {
        "bojTagId": 7,
        "key": "graphs"
      },
      {
        "bojTagId": 11,
        "key": "graph_traversal"
      }
    ],
    "lastupdate": 1687116861.589876
  },
  "1753": {
    "problemId": "1753",
    "problemLevel": 12,
    "problemName": "최단경로",
    "average_try": 4,
    "solvedtags": [
      {
        "bojTagId": 22,
        "key": "dijkstra"
      },
      {
        "bojTagId": 7,
        "key": "graphs"
      }
    ],
    "lastupdate": 1687116861.589901
  },
  "1916": {
    "problemId": "1916",
    "problemLevel": 11,
    "problemName": "최소비용 구하기",
    "average_try": 3.1052,
    "solvedtags": [
      {
        "bojTagId": 22,
        "key": "dijkstra"
      },
      {
        "bojTagId": 7,
        "key": "graphs"
      }
    ],
    "lastupdate": 1687116861.589921
  },
  "13549": {
    "problemId": "13549",
    "problemLevel": 11,
    "problemName": "숨바꼭질 3",
    "average_try": 4.0036,
    "solvedtags": [
      {
        "bojTagId": 176,
        "key": "0_1_bfs"
      },
      {
        "bojTagId": 126,
        "key": "bfs"
      },
      {
        "bojTagId": 22,
        "key": "dijkstra"
      },
      {
        "bojTagId": 7,
        "key": "graphs"
      },
      {
        "bojTagId": 11,
        "key": "graph_traversal"
      }
    ],
    "lastupdate": 1687116861.58994
  },
  "1446": {
    "problemId": "1446",
    "problemLevel": 10,
    "problemName": "지름길",
    "average_try": 1.8955,
    "solvedtags": [
      {
        "bojTagId": 22,
        "key": "dijkstra"
      },
      {
        "bojTagId": 25,
        "key": "dp"
      },
      {
        "bojTagId": 7,
        "key": "graphs"
      }
    ],
    "lastupdate": 1687116861.589959
  },
  "13424": {
    "problemId": "13424",
    "problemLevel": 12,
    "problemName": "비밀 모임",
    "average_try": 1.9551,
    "solvedtags": [
      {
        "bojTagId": 22,
        "key": "dijkstra"
      },
      {
        "bojTagId": 31,
        "key": "floyd_warshall"
      },
      {
        "bojTagId": 7,
        "key": "graphs"
      }
    ],
    "lastupdate": 1687116861.589977
  },
  "17396": {
    "problemId": "17396",
    "problemLevel": 11,
    "problemName": "백도어",
    "average_try": 4.0544,
    "solvedtags": [
      {
        "bojTagId": 22,
        "key": "dijkstra"
      },
      {
        "bojTagId": 7,
        "key": "graphs"
      }
    ],
    "lastupdate": 1687116861.590006
  },
  "5972": {
    "problemId": "5972",
    "problemLevel": 11,
    "problemName": "택배 배송",
    "average_try": 1.6302,
    "solvedtags": [
      {
        "bojTagId": 22,
        "key": "dijkstra"
      },
      {
        "bojTagId": 7,
        "key": "graphs"
      }
    ],
    "lastupdate": 1687116861.590036
  },
  "14284": {
    "problemId": "14284",
    "problemLevel": 11,
    "problemName": "간선 이어가기 2",
    "average_try": 1.7487,
    "solvedtags": [
      {
        "bojTagId": 22,
        "key": "dijkstra"
      },
      {
        "bojTagId": 7,
        "key": "graphs"
      }
    ],
    "lastupdate": 1687116861.590055
  },
  "20168": {
    "problemId": "20168",
    "problemLevel": 11,
    "problemName": "골목 대장 호석 - 기능성",
    "average_try": 2.659,
    "solvedtags": [
      {
        "bojTagId": 5,
        "key": "backtracking"
      },
      {
        "bojTagId": 125,
        "key": "bruteforcing"
      },
      {
        "bojTagId": 22,
        "key": "dijkstra"
      },
      {
        "bojTagId": 7,
        "key": "graphs"
      }
    ],
    "lastupdate": 1687116861.590073
  },
  "20182": {
    "problemId": "20182",
    "problemLevel": 13,
    "problemName": "골목 대장 호석 - 효율성 1",
    "average_try": 2.7409,
    "solvedtags": [
      {
        "bojTagId": 22,
        "key": "dijkstra"
      },
      {
        "bojTagId": 7,
        "key": "graphs"
      }
    ],
    "lastupdate": 1687116861.59009
  },
  "20183": {
    "problemId": "20183",
    "problemLevel": 14,
    "problemName": "골목 대장 호석 - 효율성 2",
    "average_try": 4.2743,
    "solvedtags": [
      {
        "bojTagId": 12,
        "key": "binary_search"
      },
      {
        "bojTagId": 22,
        "key": "dijkstra"
      },
      {
        "bojTagId": 7,
        "key": "graphs"
      },
      {
        "bojTagId": 170,
        "key": "parametric_search"
      }
    ],
    "lastupdate": 1687116861.590108
  },
  "1261": {
    "problemId": "1261",
    "problemLevel": 12,
    "problemName": "알고스팟",
    "average_try": 2.38,
    "solvedtags": [
      {
        "bojTagId": 176,
        "key": "0_1_bfs"
      },
      {
        "bojTagId": 22,
        "key": "dijkstra"
      },
      {
        "bojTagId": 7,
        "key": "graphs"
      },
      {
        "bojTagId": 11,
        "key": "graph_traversal"
      }
    ],
    "lastupdate": 1687116861.590126
  },
  "1504": {
    "problemId": "1504",
    "problemLevel": 12,
    "problemName": "특정한 최단 경로",
    "average_try": 4.0792,
    "solvedtags": [
      {
        "bojTagId": 22,
        "key": "dijkstra"
      },
      {
        "bojTagId": 7,
        "key": "graphs"
      }
    ],
    "lastupdate": 1687116861.590144
  },
  "4485": {
    "problemId": "4485",
    "problemLevel": 12,
    "problemName": "녹색 옷 입은 애가 젤다지?",
    "average_try": 1.9584,
    "solvedtags": [
      {
        "bojTagId": 22,
        "key": "dijkstra"
      },
      {
        "bojTagId": 7,
        "key": "graphs"
      }
    ],
    "lastupdate": 1687116861.590162
  },
  "10282": {
    "problemId": "10282",
    "problemLevel": 12,
    "problemName": "해킹",
    "average_try": 2.5299,
    "solvedtags": [
      {
        "bojTagId": 22,
        "key": "dijkstra"
      },
      {
        "bojTagId": 7,
        "key": "graphs"
      }
    ],
    "lastupdate": 1687116861.59018
  },
  "14938": {
    "problemId": "14938",
    "problemLevel": 12,
    "problemName": "서강그라운드",
    "average_try": 1.9676,
    "solvedtags": [
      {
        "bojTagId": 22,
        "key": "dijkstra"
      },
      {
        "bojTagId": 31,
        "key": "floyd_warshall"
      },
      {
        "bojTagId": 7,
        "key": "graphs"
      }
    ],
    "lastupdate": 1687116861.590198
  },
  "1719": {
    "problemId": "1719",
    "problemLevel": 13,
    "problemName": "택배",
    "average_try": 1.7523,
    "solvedtags": [
      {
        "bojTagId": 22,
        "key": "dijkstra"
      },
      {
        "bojTagId": 31,
        "key": "floyd_warshall"
      },
      {
        "bojTagId": 7,
        "key": "graphs"
      }
    ],
    "lastupdate": 1687116861.590216
  },
  "18223": {
    "problemId": "18223",
    "problemLevel": 12,
    "problemName": "민준이와 마산 그리고 건우",
    "average_try": 1.9479,
    "solvedtags": [
      {
        "bojTagId": 22,
        "key": "dijkstra"
      },
      {
        "bojTagId": 7,
        "key": "graphs"
      }
    ],
    "lastupdate": 1687116861.590234
  },
  "20007": {
    "problemId": "20007",
    "problemLevel": 12,
    "problemName": "떡 돌리기",
    "average_try": 2.6364,
    "solvedtags": [
      {
        "bojTagId": 22,
        "key": "dijkstra"
      },
      {
        "bojTagId": 7,
        "key": "graphs"
      }
    ],
    "lastupdate": 1687116861.590251
  },
  "1277": {
    "problemId": "1277",
    "problemLevel": 12,
    "problemName": "발전소 설치",
    "average_try": 3.6884,
    "solvedtags": [
      {
        "bojTagId": 22,
        "key": "dijkstra"
      },
      {
        "bojTagId": 7,
        "key": "graphs"
      }
    ],
    "lastupdate": 1687116861.590269
  },
  "1238": {
    "problemId": "1238",
    "problemLevel": 13,
    "problemName": "파티",
    "average_try": 2.0825,
    "solvedtags": [
      {
        "bojTagId": 22,
        "key": "dijkstra"
      },
      {
        "bojTagId": 7,
        "key": "graphs"
      }
    ],
    "lastupdate": 1687116861.590286
  },
  "11779": {
    "problemId": "11779",
    "problemLevel": 13,
    "problemName": "최소비용 구하기 2",
    "average_try": 2.7617,
    "solvedtags": [
      {
        "bojTagId": 22,
        "key": "dijkstra"
      },
      {
        "bojTagId": 7,
        "key": "graphs"
      }
    ],
    "lastupdate": 1687116861.590303
  },
  "13911": {
    "problemId": "13911",
    "problemLevel": 14,
    "problemName": "집 구하기",
    "average_try": 3.8985,
    "solvedtags": [
      {
        "bojTagId": 22,
        "key": "dijkstra"
      },
      {
        "bojTagId": 7,
        "key": "graphs"
      }
    ],
    "lastupdate": 1687116861.59032
  },
  "2982": {
    "problemId": "2982",
    "problemLevel": 14,
    "problemName": "국왕의 방문",
    "average_try": 2.2799,
    "solvedtags": [
      {
        "bojTagId": 22,
        "key": "dijkstra"
      },
      {
        "bojTagId": 7,
        "key": "graphs"
      }
    ],
    "lastupdate": 1687116861.590338
  },
  "9370": {
    "problemId": "9370",
    "problemLevel": 14,
    "problemName": "미확인 도착지",
    "average_try": 4.0261,
    "solvedtags": [
      {
        "bojTagId": 22,
        "key": "dijkstra"
      },
      {
        "bojTagId": 7,
        "key": "graphs"
      }
    ],
    "lastupdate": 1687116861.590355
  },
  "2211": {
    "problemId": "2211",
    "problemLevel": 14,
    "problemName": "네트워크 복구",
    "average_try": 2.0169,
    "solvedtags": [
      {
        "bojTagId": 22,
        "key": "dijkstra"
      },
      {
        "bojTagId": 7,
        "key": "graphs"
      }
    ],
    "lastupdate": 1687116861.590373
  },
  "16118": {
    "problemId": "16118",
    "problemLevel": 15,
    "problemName": "달빛 여우",
    "average_try": 5.1509,
    "solvedtags": [
      {
        "bojTagId": 22,
        "key": "dijkstra"
      },
      {
        "bojTagId": 7,
        "key": "graphs"
      }
    ],
    "lastupdate": 1687116861.590391
  },
  "1445": {
    "problemId": "1445",
    "problemLevel": 14,
    "problemName": "일요일 아침의 데이트",
    "average_try": 4.1124,
    "solvedtags": [
      {
        "bojTagId": 175,
        "key": "data_structures"
      },
      {
        "bojTagId": 22,
        "key": "dijkstra"
      },
      {
        "bojTagId": 7,
        "key": "graphs"
      }
    ],
    "lastupdate": 1687116861.590408
  },
  "2307": {
    "problemId": "2307",
    "problemLevel": 15,
    "problemName": "도로검문",
    "average_try": 2.7013,
    "solvedtags": [
      {
        "bojTagId": 22,
        "key": "dijkstra"
      },
      {
        "bojTagId": 7,
        "key": "graphs"
      }
    ],
    "lastupdate": 1687116861.590425
  },
  "18243": {
    "problemId": "18243",
    "problemLevel": 10,
    "problemName": "Small World Network",
    "average_try": 2.1452,
    "solvedtags": [
      {
        "bojTagId": 126,
        "key": "bfs"
      },
      {
        "bojTagId": 31,
        "key": "floyd_warshall"
      },
      {
        "bojTagId": 7,
        "key": "graphs"
      },
      {
        "bojTagId": 11,
        "key": "graph_traversal"
      }
    ],
    "lastupdate": 1687116861.590443
  },
  "11403": {
    "problemId": "11403",
    "problemLevel": 10,
    "problemName": "경로 찾기",
    "average_try": 1.6707,
    "solvedtags": [
      {
        "bojTagId": 31,
        "key": "floyd_warshall"
      },
      {
        "bojTagId": 7,
        "key": "graphs"
      },
      {
        "bojTagId": 11,
        "key": "graph_traversal"
      }
    ],
    "lastupdate": 1687116861.59046
  },
  "1389": {
    "problemId": "1389",
    "problemLevel": 10,
    "problemName": "케빈 베이컨의 6단계 법칙",
    "average_try": 1.7855,
    "solvedtags": [
      {
        "bojTagId": 126,
        "key": "bfs"
      },
      {
        "bojTagId": 31,
        "key": "floyd_warshall"
      },
      {
        "bojTagId": 7,
        "key": "graphs"
      },
      {
        "bojTagId": 11,
        "key": "graph_traversal"
      }
    ],
    "lastupdate": 1687116861.590478
  },
  "9205": {
    "problemId": "9205",
    "problemLevel": 11,
    "problemName": "맥주 마시면서 걸어가기",
    "average_try": 2.5172,
    "solvedtags": [
      {
        "bojTagId": 126,
        "key": "bfs"
      },
      {
        "bojTagId": 7,
        "key": "graphs"
      },
      {
        "bojTagId": 11,
        "key": "graph_traversal"
      }
    ],
    "lastupdate": 1687116861.590499
  },
  "1058": {
    "problemId": "1058",
    "problemLevel": 9,
    "problemName": "친구",
    "average_try": 2.2122,
    "solvedtags": [
      {
        "bojTagId": 125,
        "key": "bruteforcing"
      },
      {
        "bojTagId": 31,
        "key": "floyd_warshall"
      },
      {
        "bojTagId": 7,
        "key": "graphs"
      },
      {
        "bojTagId": 11,
        "key": "graph_traversal"
      }
    ],
    "lastupdate": 1687116861.590517
  },
  "2224": {
    "problemId": "2224",
    "problemLevel": 12,
    "problemName": "명제 증명",
    "average_try": 3.3672,
    "solvedtags": [
      {
        "bojTagId": 31,
        "key": "floyd_warshall"
      },
      {
        "bojTagId": 7,
        "key": "graphs"
      }
    ],
    "lastupdate": 1687116861.590534
  },
  "11265": {
    "problemId": "11265",
    "problemLevel": 11,
    "problemName": "끝나지 않는 파티",
    "average_try": 1.9705,
    "solvedtags": [
      {
        "bojTagId": 31,
        "key": "floyd_warshall"
      },
      {
        "bojTagId": 7,
        "key": "graphs"
      }
    ],
    "lastupdate": 1687116861.590552
  },
  "2660": {
    "problemId": "2660",
    "problemLevel": 11,
    "problemName": "회장뽑기",
    "average_try": 1.8189,
    "solvedtags": [
      {
        "bojTagId": 126,
        "key": "bfs"
      },
      {
        "bojTagId": 31,
        "key": "floyd_warshall"
      },
      {
        "bojTagId": 7,
        "key": "graphs"
      },
      {
        "bojTagId": 11,
        "key": "graph_traversal"
      }
    ],
    "lastupdate": 1687116861.590569
  },
  "15723": {
    "problemId": "15723",
    "problemLevel": 10,
    "problemName": "n단 논법",
    "average_try": 1.6948,
    "solvedtags": [
      {
        "bojTagId": 126,
        "key": "bfs"
      },
      {
        "bojTagId": 127,
        "key": "dfs"
      },
      {
        "bojTagId": 31,
        "key": "floyd_warshall"
      },
      {
        "bojTagId": 7,
        "key": "graphs"
      },
      {
        "bojTagId": 11,
        "key": "graph_traversal"
      }
    ],
    "lastupdate": 1687116861.590587
  },
  "11404": {
    "problemId": "11404",
    "problemLevel": 12,
    "problemName": "플로이드",
    "average_try": 2.4068,
    "solvedtags": [
      {
        "bojTagId": 31,
        "key": "floyd_warshall"
      },
      {
        "bojTagId": 7,
        "key": "graphs"
      }
    ],
    "lastupdate": 1687116861.590604
  },
  "2458": {
    "problemId": "2458",
    "problemLevel": 12,
    "problemName": "키 순서",
    "average_try": 1.8602,
    "solvedtags": [
      {
        "bojTagId": 31,
        "key": "floyd_warshall"
      },
      {
        "bojTagId": 7,
        "key": "graphs"
      },
      {
        "bojTagId": 11,
        "key": "graph_traversal"
      }
    ],
    "lastupdate": 1687116861.590622
  },
  "1956": {
    "problemId": "1956",
    "problemLevel": 12,
    "problemName": "운동",
    "average_try": 2.4867,
    "solvedtags": [
      {
        "bojTagId": 31,
        "key": "floyd_warshall"
      },
      {
        "bojTagId": 7,
        "key": "graphs"
      }
    ],
    "lastupdate": 1687116861.59064
  },
  "11562": {
    "problemId": "11562",
    "problemLevel": 13,
    "problemName": "백양로 브레이크",
    "average_try": 2.0869,
    "solvedtags": [
      {
        "bojTagId": 31,
        "key": "floyd_warshall"
      },
      {
        "bojTagId": 7,
        "key": "graphs"
      }
    ],
    "lastupdate": 1687116861.590657
  },
  "10159": {
    "problemId": "10159",
    "problemLevel": 12,
    "problemName": "저울",
    "average_try": 1.5127,
    "solvedtags": [
      {
        "bojTagId": 31,
        "key": "floyd_warshall"
      },
      {
        "bojTagId": 7,
        "key": "graphs"
      },
      {
        "bojTagId": 11,
        "key": "graph_traversal"
      }
    ],
    "lastupdate": 1687116861.590675
  },
  "1507": {
    "problemId": "1507",
    "problemLevel": 14,
    "problemName": "궁금한 민호",
    "average_try": 1.9288,
    "solvedtags": [
      {
        "bojTagId": 31,
        "key": "floyd_warshall"
      },
      {
        "bojTagId": 7,
        "key": "graphs"
      }
    ],
    "lastupdate": 1687116861.590693
  },
  "1613": {
    "problemId": "1613",
    "problemLevel": 13,
    "problemName": "역사",
    "average_try": 2.9643,
    "solvedtags": [
      {
        "bojTagId": 31,
        "key": "floyd_warshall"
      },
      {
        "bojTagId": 7,
        "key": "graphs"
      }
    ],
    "lastupdate": 1687116861.590711
  },
  "11780": {
    "problemId": "11780",
    "problemLevel": 14,
    "problemName": "플로이드 2",
    "average_try": 2.2023,
    "solvedtags": [
      {
        "bojTagId": 31,
        "key": "floyd_warshall"
      },
      {
        "bojTagId": 7,
        "key": "graphs"
      }
    ],
    "lastupdate": 1687116861.590728
  },
  "11657": {
    "problemId": "11657",
    "problemLevel": 12,
    "problemName": "타임머신",
    "average_try": 4.2544,
    "solvedtags": [
      {
        "bojTagId": 10,
        "key": "bellman_ford"
      },
      {
        "bojTagId": 7,
        "key": "graphs"
      }
    ],
    "lastupdate": 1687116861.590745
  },
  "1865": {
    "problemId": "1865",
    "problemLevel": 13,
    "problemName": "웜홀",
    "average_try": 4.5823,
    "solvedtags": [
      {
        "bojTagId": 10,
        "key": "bellman_ford"
      },
      {
        "bojTagId": 7,
        "key": "graphs"
      }
    ],
    "lastupdate": 1687116861.590763
  },
  "1219": {
    "problemId": "1219",
    "problemLevel": 16,
    "problemName": "오민식의 고민",
    "average_try": 5.8351,
    "solvedtags": [
      {
        "bojTagId": 10,
        "key": "bellman_ford"
      },
      {
        "bojTagId": 7,
        "key": "graphs"
      },
      {
        "bojTagId": 11,
        "key": "graph_traversal"
      }
    ],
    "lastupdate": 1687116861.59078
  },
  "21940": {
    "problemId": "21940",
    "problemLevel": 12,
    "problemName": "가운데에서 만나기",
    "average_try": 2.2874,
    "solvedtags": [
      {
        "bojTagId": 31,
        "key": "floyd_warshall"
      },
      {
        "bojTagId": 7,
        "key": "graphs"
      }
    ],
    "lastupdate": 1687116861.590797
  },
  "22865": {
    "problemId": "22865",
    "problemLevel": 12,
    "problemName": "가장 먼 곳",
    "average_try": 3.0798,
    "solvedtags": [
      {
        "bojTagId": 22,
        "key": "dijkstra"
      },
      {
        "bojTagId": 7,
        "key": "graphs"
      }
    ],
    "lastupdate": 1687116861.590815
  },
  "22870": {
    "problemId": "22870",
    "problemLevel": 16,
    "problemName": "산책 (large)",
    "average_try": 6.7375,
    "solvedtags": [
      {
        "bojTagId": 22,
        "key": "dijkstra"
      },
      {
        "bojTagId": 7,
        "key": "graphs"
      },
      {
        "bojTagId": 11,
        "key": "graph_traversal"
      }
    ],
    "lastupdate": 1687116861.590833
  },
  "20436": {
    "problemId": "20436",
    "problemLevel": 7,
    "problemName": "ZOAC 3",
    "average_try": 2.129,
    "solvedtags": [
      {
        "bojTagId": 102,
        "key": "implementation"
      },
      {
        "bojTagId": 141,
        "key": "simulation"
      }
    ],
    "lastupdate": 1687116861.591584
  },
  "14594": {
    "problemId": "14594",
    "problemLevel": 7,
    "problemName": "동방 프로젝트 (Small)",
    "average_try": 1.5888,
    "solvedtags": [
      {
        "bojTagId": 102,
        "key": "implementation"
      },
      {
        "bojTagId": 141,
        "key": "simulation"
      }
    ],
    "lastupdate": 1687116861.591608
  },
  "5212": {
    "problemId": "5212",
    "problemLevel": 9,
    "problemName": "지구 온난화",
    "average_try": 1.8163,
    "solvedtags": [
      {
        "bojTagId": 102,
        "key": "implementation"
      },
      {
        "bojTagId": 141,
        "key": "simulation"
      }
    ],
    "lastupdate": 1687116861.591628
  },
  "14891": {
    "problemId": "14891",
    "problemLevel": 11,
    "problemName": "톱니바퀴",
    "average_try": 1.8334,
    "solvedtags": [
      {
        "bojTagId": 102,
        "key": "implementation"
      },
      {
        "bojTagId": 141,
        "key": "simulation"
      }
    ],
    "lastupdate": 1687116861.591647
  },
  "1713": {
    "problemId": "1713",
    "problemLevel": 10,
    "problemName": "후보 추천하기",
    "average_try": 3.2208,
    "solvedtags": [
      {
        "bojTagId": 102,
        "key": "implementation"
      },
      {
        "bojTagId": 141,
        "key": "simulation"
      }
    ],
    "lastupdate": 1687116861.591666
  },
  "20055": {
    "problemId": "20055",
    "problemLevel": 11,
    "problemName": "컨베이어 벨트 위의 로봇",
    "average_try": 1.7575,
    "solvedtags": [
      {
        "bojTagId": 102,
        "key": "implementation"
      },
      {
        "bojTagId": 141,
        "key": "simulation"
      }
    ],
    "lastupdate": 1687116861.591684
  },
  "20665": {
    "problemId": "20665",
    "problemLevel": 11,
    "problemName": "독서실 거리두기",
    "average_try": 4.2841,
    "solvedtags": [
      {
        "bojTagId": 102,
        "key": "implementation"
      },
      {
        "bojTagId": 141,
        "key": "simulation"
      }
    ],
    "lastupdate": 1687116861.591703
  },
  "14503": {
    "problemId": "14503",
    "problemLevel": 11,
    "problemName": "로봇 청소기",
    "average_try": 1.8624,
    "solvedtags": [
      {
        "bojTagId": 102,
        "key": "implementation"
      },
      {
        "bojTagId": 141,
        "key": "simulation"
      }
    ],
    "lastupdate": 1687116861.591733
  },
  "3190": {
    "problemId": "3190",
    "problemLevel": 12,
    "problemName": "뱀",
    "average_try": 2.5031,
    "solvedtags": [
      {
        "bojTagId": 175,
        "key": "data_structures"
      },
      {
        "bojTagId": 73,
        "key": "deque"
      },
      {
        "bojTagId": 102,
        "key": "implementation"
      },
      {
        "bojTagId": 72,
        "key": "queue"
      },
      {
        "bojTagId": 141,
        "key": "simulation"
      }
    ],
    "lastupdate": 1687116861.591752
  },
  "14499": {
    "problemId": "14499",
    "problemLevel": 12,
    "problemName": "주사위 굴리기",
    "average_try": 2.2566,
    "solvedtags": [
      {
        "bojTagId": 102,
        "key": "implementation"
      },
      {
        "bojTagId": 141,
        "key": "simulation"
      }
    ],
    "lastupdate": 1687116861.59177
  },
  "15683": {
    "problemId": "15683",
    "problemLevel": 12,
    "problemName": "감시",
    "average_try": 2.2811,
    "solvedtags": [
      {
        "bojTagId": 5,
        "key": "backtracking"
      },
      {
        "bojTagId": 125,
        "key": "bruteforcing"
      },
      {
        "bojTagId": 102,
        "key": "implementation"
      },
      {
        "bojTagId": 141,
        "key": "simulation"
      }
    ],
    "lastupdate": 1687116861.591788
  },
  "16234": {
    "problemId": "16234",
    "problemLevel": 11,
    "problemName": "인구 이동",
    "average_try": 2.6868,
    "solvedtags": [
      {
        "bojTagId": 126,
        "key": "bfs"
      },
      {
        "bojTagId": 7,
        "key": "graphs"
      },
      {
        "bojTagId": 11,
        "key": "graph_traversal"
      },
      {
        "bojTagId": 102,
        "key": "implementation"
      },
      {
        "bojTagId": 141,
        "key": "simulation"
      }
    ],
    "lastupdate": 1687116861.591806
  },
  "17144": {
    "problemId": "17144",
    "problemLevel": 12,
    "problemName": "미세먼지 안녕!",
    "average_try": 1.844,
    "solvedtags": [
      {
        "bojTagId": 102,
        "key": "implementation"
      },
      {
        "bojTagId": 141,
        "key": "simulation"
      }
    ],
    "lastupdate": 1687116861.591824
  },
  "20056": {
    "problemId": "20056",
    "problemLevel": 12,
    "problemName": "마법사 상어와 파이어볼",
    "average_try": 2.7538,
    "solvedtags": [
      {
        "bojTagId": 102,
        "key": "implementation"
      },
      {
        "bojTagId": 141,
        "key": "simulation"
      }
    ],
    "lastupdate": 1687116861.591842
  },
  "20165": {
    "problemId": "20165",
    "problemLevel": 11,
    "problemName": "인내의 도미노 장인 호석",
    "average_try": 2.3935,
    "solvedtags": [
      {
        "bojTagId": 102,
        "key": "implementation"
      },
      {
        "bojTagId": 141,
        "key": "simulation"
      }
    ],
    "lastupdate": 1687116861.591859
  },
  "16236": {
    "problemId": "16236",
    "problemLevel": 13,
    "problemName": "아기 상어",
    "average_try": 2.3415,
    "solvedtags": [
      {
        "bojTagId": 126,
        "key": "bfs"
      },
      {
        "bojTagId": 7,
        "key": "graphs"
      },
      {
        "bojTagId": 11,
        "key": "graph_traversal"
      },
      {
        "bojTagId": 102,
        "key": "implementation"
      },
      {
        "bojTagId": 141,
        "key": "simulation"
      }
    ],
    "lastupdate": 1687116861.591877
  },
  "15685": {
    "problemId": "15685",
    "problemLevel": 12,
    "problemName": "드래곤 커브",
    "average_try": 1.8202,
    "solvedtags": [
      {
        "bojTagId": 102,
        "key": "implementation"
      },
      {
        "bojTagId": 141,
        "key": "simulation"
      }
    ],
    "lastupdate": 1687116861.591895
  },
  "16235": {
    "problemId": "16235",
    "problemLevel": 13,
    "problemName": "나무 재테크",
    "average_try": 4.5638,
    "solvedtags": [
      {
        "bojTagId": 175,
        "key": "data_structures"
      },
      {
        "bojTagId": 102,
        "key": "implementation"
      },
      {
        "bojTagId": 141,
        "key": "simulation"
      }
    ],
    "lastupdate": 1687116861.591913
  },
  "17135": {
    "problemId": "17135",
    "problemLevel": 13,
    "problemName": "캐슬 디펜스",
    "average_try": 3.0836,
    "solvedtags": [
      {
        "bojTagId": 126,
        "key": "bfs"
      },
      {
        "bojTagId": 125,
        "key": "bruteforcing"
      },
      {
        "bojTagId": 7,
        "key": "graphs"
      },
      {
        "bojTagId": 11,
        "key": "graph_traversal"
      },
      {
        "bojTagId": 102,
        "key": "implementation"
      },
      {
        "bojTagId": 141,
        "key": "simulation"
      }
    ],
    "lastupdate": 1687116861.59193
  },
  "17140": {
    "problemId": "17140",
    "problemLevel": 12,
    "problemName": "이차원 배열과 연산",
    "average_try": 2.2715,
    "solvedtags": [
      {
        "bojTagId": 102,
        "key": "implementation"
      },
      {
        "bojTagId": 141,
        "key": "simulation"
      },
      {
        "bojTagId": 97,
        "key": "sorting"
      }
    ],
    "lastupdate": 1687116861.591947
  },
  "17779": {
    "problemId": "17779",
    "problemLevel": 13,
    "problemName": "게리맨더링 2",
    "average_try": 1.7503,
    "solvedtags": [
      {
        "bojTagId": 125,
        "key": "bruteforcing"
      },
      {
        "bojTagId": 102,
        "key": "implementation"
      },
      {
        "bojTagId": 141,
        "key": "simulation"
      }
    ],
    "lastupdate": 1687116861.591965
  },
  "19238": {
    "problemId": "19238",
    "problemLevel": 14,
    "problemName": "스타트 택시",
    "average_try": 4.784,
    "solvedtags": [
      {
        "bojTagId": 126,
        "key": "bfs"
      },
      {
        "bojTagId": 7,
        "key": "graphs"
      },
      {
        "bojTagId": 11,
        "key": "graph_traversal"
      },
      {
        "bojTagId": 102,
        "key": "implementation"
      },
      {
        "bojTagId": 141,
        "key": "simulation"
      }
    ],
    "lastupdate": 1687116861.591982
  },
  "20057": {
    "problemId": "20057",
    "problemLevel": 13,
    "problemName": "마법사 상어와 토네이도",
    "average_try": 1.4097,
    "solvedtags": [
      {
        "bojTagId": 102,
        "key": "implementation"
      },
      {
        "bojTagId": 141,
        "key": "simulation"
      }
    ],
    "lastupdate": 1687116861.591999
  },
  "20058": {
    "problemId": "20058",
    "problemLevel": 13,
    "problemName": "마법사 상어와 파이어스톰",
    "average_try": 2.5415,
    "solvedtags": [
      {
        "bojTagId": 126,
        "key": "bfs"
      },
      {
        "bojTagId": 127,
        "key": "dfs"
      },
      {
        "bojTagId": 7,
        "key": "graphs"
      },
      {
        "bojTagId": 11,
        "key": "graph_traversal"
      },
      {
        "bojTagId": 102,
        "key": "implementation"
      },
      {
        "bojTagId": 141,
        "key": "simulation"
      }
    ],
    "lastupdate": 1687116861.592016
  },
  "8972": {
    "problemId": "8972",
    "problemLevel": 13,
    "problemName": "미친 아두이노",
    "average_try": 3.4382,
    "solvedtags": [
      {
        "bojTagId": 102,
        "key": "implementation"
      },
      {
        "bojTagId": 141,
        "key": "simulation"
      }
    ],
    "lastupdate": 1687116861.592034
  },
  "17822": {
    "problemId": "17822",
    "problemLevel": 14,
    "problemName": "원판 돌리기",
    "average_try": 2.997,
    "solvedtags": [
      {
        "bojTagId": 102,
        "key": "implementation"
      },
      {
        "bojTagId": 141,
        "key": "simulation"
      }
    ],
    "lastupdate": 1687116861.592052
  },
  "19236": {
    "problemId": "19236",
    "problemLevel": 14,
    "problemName": "청소년 상어",
    "average_try": 1.5447,
    "solvedtags": [
      {
        "bojTagId": 5,
        "key": "backtracking"
      },
      {
        "bojTagId": 102,
        "key": "implementation"
      },
      {
        "bojTagId": 141,
        "key": "simulation"
      }
    ],
    "lastupdate": 1687116861.592069
  },
  "13459": {
    "problemId": "13459",
    "problemLevel": 15,
    "problemName": "구슬 탈출",
    "average_try": 2.8744,
    "solvedtags": [
      {
        "bojTagId": 126,
        "key": "bfs"
      },
      {
        "bojTagId": 7,
        "key": "graphs"
      },
      {
        "bojTagId": 11,
        "key": "graph_traversal"
      },
      {
        "bojTagId": 102,
        "key": "implementation"
      },
      {
        "bojTagId": 141,
        "key": "simulation"
      }
    ],
    "lastupdate": 1687116861.592087
  },
  "2933": {
    "problemId": "2933",
    "problemLevel": 14,
    "problemName": "미네랄",
    "average_try": 3.9303,
    "solvedtags": [
      {
        "bojTagId": 126,
        "key": "bfs"
      },
      {
        "bojTagId": 7,
        "key": "graphs"
      },
      {
        "bojTagId": 11,
        "key": "graph_traversal"
      },
      {
        "bojTagId": 102,
        "key": "implementation"
      },
      {
        "bojTagId": 141,
        "key": "simulation"
      }
    ],
    "lastupdate": 1687116861.592105
  },
  "19237": {
    "problemId": "19237",
    "problemLevel": 14,
    "problemName": "어른 상어",
    "average_try": 2.5697,
    "solvedtags": [
      {
        "bojTagId": 102,
        "key": "implementation"
      },
      {
        "bojTagId": 141,
        "key": "simulation"
      }
    ],
    "lastupdate": 1687116861.592122
  },
  "18808": {
    "problemId": "18808",
    "problemLevel": 13,
    "problemName": "스티커 붙이기",
    "average_try": 1.5973,
    "solvedtags": [
      {
        "bojTagId": 125,
        "key": "bruteforcing"
      },
      {
        "bojTagId": 102,
        "key": "implementation"
      },
      {
        "bojTagId": 141,
        "key": "simulation"
      }
    ],
    "lastupdate": 1687116861.592139
  },
  "18500": {
    "problemId": "18500",
    "problemLevel": 15,
    "problemName": "미네랄 2",
    "average_try": 2.8307,
    "solvedtags": [
      {
        "bojTagId": 126,
        "key": "bfs"
      },
      {
        "bojTagId": 7,
        "key": "graphs"
      },
      {
        "bojTagId": 11,
        "key": "graph_traversal"
      },
      {
        "bojTagId": 102,
        "key": "implementation"
      },
      {
        "bojTagId": 141,
        "key": "simulation"
      }
    ],
    "lastupdate": 1687116861.592156
  },
  "17143": {
    "problemId": "17143",
    "problemLevel": 15,
    "problemName": "낚시왕",
    "average_try": 3.7726,
    "solvedtags": [
      {
        "bojTagId": 102,
        "key": "implementation"
      },
      {
        "bojTagId": 141,
        "key": "simulation"
      }
    ],
    "lastupdate": 1687116861.592173
  },
  "17837": {
    "problemId": "17837",
    "problemLevel": 14,
    "problemName": "새로운 게임 2",
    "average_try": 2.1223,
    "solvedtags": [
      {
        "bojTagId": 102,
        "key": "implementation"
      },
      {
        "bojTagId": 141,
        "key": "simulation"
      }
    ],
    "lastupdate": 1687116861.59219
  },
  "15653": {
    "problemId": "15653",
    "problemLevel": 15,
    "problemName": "구슬 탈출 4",
    "average_try": 2.1686,
    "solvedtags": [
      {
        "bojTagId": 126,
        "key": "bfs"
      },
      {
        "bojTagId": 7,
        "key": "graphs"
      },
      {
        "bojTagId": 11,
        "key": "graph_traversal"
      },
      {
        "bojTagId": 102,
        "key": "implementation"
      },
      {
        "bojTagId": 141,
        "key": "simulation"
      }
    ],
    "lastupdate": 1687116861.592208
  },
  "17780": {
    "problemId": "17780",
    "problemLevel": 14,
    "problemName": "새로운 게임",
    "average_try": 2.0229,
    "solvedtags": [
      {
        "bojTagId": 102,
        "key": "implementation"
      },
      {
        "bojTagId": 141,
        "key": "simulation"
      }
    ],
    "lastupdate": 1687116861.592226
  },
  "20061": {
    "problemId": "20061",
    "problemLevel": 14,
    "problemName": "모노미노도미노 2",
    "average_try": 2.8927,
    "solvedtags": [
      {
        "bojTagId": 102,
        "key": "implementation"
      },
      {
        "bojTagId": 141,
        "key": "simulation"
      }
    ],
    "lastupdate": 1687116861.592244
  },
  "5373": {
    "problemId": "5373",
    "problemLevel": 16,
    "problemName": "큐빙",
    "average_try": 2.602,
    "solvedtags": [
      {
        "bojTagId": 102,
        "key": "implementation"
      },
      {
        "bojTagId": 141,
        "key": "simulation"
      }
    ],
    "lastupdate": 1687116861.592261
  },
  "18809": {
    "problemId": "18809",
    "problemLevel": 15,
    "problemName": "Gaaaaaaaaaarden",
    "average_try": 2.2645,
    "solvedtags": [
      {
        "bojTagId": 126,
        "key": "bfs"
      },
      {
        "bojTagId": 125,
        "key": "bruteforcing"
      },
      {
        "bojTagId": 7,
        "key": "graphs"
      },
      {
        "bojTagId": 11,
        "key": "graph_traversal"
      },
      {
        "bojTagId": 102,
        "key": "implementation"
      },
      {
        "bojTagId": 141,
        "key": "simulation"
      }
    ],
    "lastupdate": 1687116861.592279
  },
  "16939": {
    "problemId": "16939",
    "problemLevel": 14,
    "problemName": "2×2×2 큐브",
    "average_try": 2.3234,
    "solvedtags": [
      {
        "bojTagId": 102,
        "key": "implementation"
      }
    ],
    "lastupdate": 1687116861.592297
  },
  "19235": {
    "problemId": "19235",
    "problemLevel": 16,
    "problemName": "모노미노도미노",
    "average_try": 5.0398,
    "solvedtags": [
      {
        "bojTagId": 102,
        "key": "implementation"
      },
      {
        "bojTagId": 141,
        "key": "simulation"
      }
    ],
    "lastupdate": 1687116861.592314
  },
  "3025": {
    "problemId": "3025",
    "problemLevel": 17,
    "problemName": "돌 던지기",
    "average_try": 5.9557,
    "solvedtags": [
      {
        "bojTagId": 175,
        "key": "data_structures"
      },
      {
        "bojTagId": 25,
        "key": "dp"
      },
      {
        "bojTagId": 102,
        "key": "implementation"
      },
      {
        "bojTagId": 141,
        "key": "simulation"
      },
      {
        "bojTagId": 71,
        "key": "stack"
      }
    ],
    "lastupdate": 1687116861.592332
  },
  "13460": {
    "problemId": "13460",
    "problemLevel": 15,
    "problemName": "구슬 탈출 2",
    "average_try": 3.6269,
    "solvedtags": [
      {
        "bojTagId": 126,
        "key": "bfs"
      },
      {
        "bojTagId": 7,
        "key": "graphs"
      },
      {
        "bojTagId": 11,
        "key": "graph_traversal"
      },
      {
        "bojTagId": 102,
        "key": "implementation"
      },
      {
        "bojTagId": 141,
        "key": "simulation"
      }
    ],
    "lastupdate": 1687116861.59235
  },
  "15644": {
    "problemId": "15644",
    "problemLevel": 15,
    "problemName": "구슬 탈출 3",
    "average_try": 1.6333,
    "solvedtags": [
      {
        "bojTagId": 126,
        "key": "bfs"
      },
      {
        "bojTagId": 7,
        "key": "graphs"
      },
      {
        "bojTagId": 11,
        "key": "graph_traversal"
      },
      {
        "bojTagId": 102,
        "key": "implementation"
      },
      {
        "bojTagId": 141,
        "key": "simulation"
      }
    ],
    "lastupdate": 1687116861.592368
  },
  "21609": {
    "problemId": "21609",
    "problemLevel": 14,
    "problemName": "상어 중학교",
    "average_try": 2.8487,
    "solvedtags": [
      {
        "bojTagId": 126,
        "key": "bfs"
      },
      {
        "bojTagId": 127,
        "key": "dfs"
      },
      {
        "bojTagId": 7,
        "key": "graphs"
      },
      {
        "bojTagId": 11,
        "key": "graph_traversal"
      },
      {
        "bojTagId": 102,
        "key": "implementation"
      },
      {
        "bojTagId": 141,
        "key": "simulation"
      }
    ],
    "lastupdate": 1687116861.592386
  },
  "21610": {
    "problemId": "21610",
    "problemLevel": 11,
    "problemName": "마법사 상어와 비바라기",
    "average_try": 2.002,
    "solvedtags": [
      {
        "bojTagId": 102,
        "key": "implementation"
      },
      {
        "bojTagId": 141,
        "key": "simulation"
      }
    ],
    "lastupdate": 1687116861.592403
  },
  "21922": {
    "problemId": "21922",
    "problemLevel": 11,
    "problemName": "학부 연구생 민상",
    "average_try": 3.8712,
    "solvedtags": [
      {
        "bojTagId": 7,
        "key": "graphs"
      },
      {
        "bojTagId": 11,
        "key": "graph_traversal"
      },
      {
        "bojTagId": 102,
        "key": "implementation"
      },
      {
        "bojTagId": 141,
        "key": "simulation"
      }
    ],
    "lastupdate": 1687116861.592421
  },
  "22861": {
    "problemId": "22861",
    "problemLevel": 15,
    "problemName": "폴더 정리 (large)",
    "average_try": 4.303,
    "solvedtags": [
      {
        "bojTagId": 175,
        "key": "data_structures"
      },
      {
        "bojTagId": 127,
        "key": "dfs"
      },
      {
        "bojTagId": 25,
        "key": "dp"
      },
      {
        "bojTagId": 92,
        "key": "dp_tree"
      },
      {
        "bojTagId": 7,
        "key": "graphs"
      },
      {
        "bojTagId": 11,
        "key": "graph_traversal"
      },
      {
        "bojTagId": 136,
        "key": "hash_set"
      },
      {
        "bojTagId": 102,
        "key": "implementation"
      },
      {
        "bojTagId": 96,
        "key": "parsing"
      },
      {
        "bojTagId": 141,
        "key": "simulation"
      },
      {
        "bojTagId": 158,
        "key": "string"
      },
      {
        "bojTagId": 120,
        "key": "trees"
      }
    ],
    "lastupdate": 1687116861.592438
  },
  "3029": {
    "problemId": "3029",
    "problemLevel": 3,
    "problemName": "경고",
    "average_try": 2.6518,
    "solvedtags": [
      {
        "bojTagId": 121,
        "key": "arithmetic"
      },
      {
        "bojTagId": 102,
        "key": "implementation"
      },
      {
        "bojTagId": 124,
        "key": "math"
      },
      {
        "bojTagId": 158,
        "key": "string"
      }
    ],
    "lastupdate": 1687116861.592976
  },
  "1942": {
    "problemId": "1942",
    "problemLevel": 4,
    "problemName": "디지털시계",
    "average_try": 1.9478,
    "solvedtags": [
      {
        "bojTagId": 102,
        "key": "implementation"
      },
      {
        "bojTagId": 124,
        "key": "math"
      },
      {
        "bojTagId": 96,
        "key": "parsing"
      },
      {
        "bojTagId": 141,
        "key": "simulation"
      },
      {
        "bojTagId": 158,
        "key": "string"
      }
    ],
    "lastupdate": 1687116861.593001
  },
  "20944": {
    "problemId": "20944",
    "problemLevel": 3,
    "problemName": "팰린드롬 척화비",
    "average_try": 1.2294,
    "solvedtags": [
      {
        "bojTagId": 109,
        "key": "ad_hoc"
      },
      {
        "bojTagId": 158,
        "key": "string"
      }
    ],
    "lastupdate": 1687116861.59302
  },
  "11720": {
    "problemId": "11720",
    "problemLevel": 2,
    "problemName": "숫자의 합",
    "average_try": 1.8025,
    "solvedtags": [
      {
        "bojTagId": 102,
        "key": "implementation"
      },
      {
        "bojTagId": 124,
        "key": "math"
      },
      {
        "bojTagId": 158,
        "key": "string"
      }
    ],
    "lastupdate": 1687116861.593039
  },
  "1152": {
    "problemId": "1152",
    "problemLevel": 4,
    "problemName": "단어의 개수",
    "average_try": 3.0719,
    "solvedtags": [
      {
        "bojTagId": 102,
        "key": "implementation"
      },
      {
        "bojTagId": 158,
        "key": "string"
      }
    ],
    "lastupdate": 1687116861.593058
  },
  "10809": {
    "problemId": "10809",
    "problemLevel": 4,
    "problemName": "알파벳 찾기",
    "average_try": 1.8822,
    "solvedtags": [
      {
        "bojTagId": 102,
        "key": "implementation"
      },
      {
        "bojTagId": 158,
        "key": "string"
      }
    ],
    "lastupdate": 1687116861.593076
  },
  "10808": {
    "problemId": "10808",
    "problemLevel": 2,
    "problemName": "알파벳 개수",
    "average_try": 1.4492,
    "solvedtags": [
      {
        "bojTagId": 102,
        "key": "implementation"
      },
      {
        "bojTagId": 158,
        "key": "string"
      }
    ],
    "lastupdate": 1687116861.593094
  },
  "11365": {
    "problemId": "11365",
    "problemLevel": 2,
    "problemName": "!밀비 급일",
    "average_try": 1.5502,
    "solvedtags": [
      {
        "bojTagId": 102,
        "key": "implementation"
      },
      {
        "bojTagId": 158,
        "key": "string"
      }
    ],
    "lastupdate": 1687116861.593112
  },
  "1159": {
    "problemId": "1159",
    "problemLevel": 4,
    "problemName": "농구 경기",
    "average_try": 1.9121,
    "solvedtags": [
      {
        "bojTagId": 102,
        "key": "implementation"
      },
      {
        "bojTagId": 158,
        "key": "string"
      }
    ],
    "lastupdate": 1687116861.59313
  },
  "2744": {
    "problemId": "2744",
    "problemLevel": 1,
    "problemName": "대소문자 바꾸기",
    "average_try": 1.2886,
    "solvedtags": [
      {
        "bojTagId": 102,
        "key": "implementation"
      },
      {
        "bojTagId": 158,
        "key": "string"
      }
    ],
    "lastupdate": 1687116861.593149
  },
  "1718": {
    "problemId": "1718",
    "problemLevel": 4,
    "problemName": "암호",
    "average_try": 1.8367,
    "solvedtags": [
      {
        "bojTagId": 102,
        "key": "implementation"
      },
      {
        "bojTagId": 158,
        "key": "string"
      }
    ],
    "lastupdate": 1687116861.593167
  },
  "9046": {
    "problemId": "9046",
    "problemLevel": 4,
    "problemName": "복호화",
    "average_try": 2.0718,
    "solvedtags": [
      {
        "bojTagId": 102,
        "key": "implementation"
      },
      {
        "bojTagId": 158,
        "key": "string"
      }
    ],
    "lastupdate": 1687116861.593185
  },
  "1032": {
    "problemId": "1032",
    "problemLevel": 5,
    "problemName": "명령 프롬프트",
    "average_try": 1.7529,
    "solvedtags": [
      {
        "bojTagId": 102,
        "key": "implementation"
      },
      {
        "bojTagId": 158,
        "key": "string"
      }
    ],
    "lastupdate": 1687116861.593203
  },
  "10798": {
    "problemId": "10798",
    "problemLevel": 5,
    "problemName": "세로읽기",
    "average_try": 1.8993,
    "solvedtags": [
      {
        "bojTagId": 102,
        "key": "implementation"
      },
      {
        "bojTagId": 158,
        "key": "string"
      }
    ],
    "lastupdate": 1687116861.593221
  },
  "10988": {
    "problemId": "10988",
    "problemLevel": 4,
    "problemName": "팰린드롬인지 확인하기",
    "average_try": 1.5449,
    "solvedtags": [
      {
        "bojTagId": 102,
        "key": "implementation"
      },
      {
        "bojTagId": 158,
        "key": "string"
      }
    ],
    "lastupdate": 1687116861.593238
  },
  "11655": {
    "problemId": "11655",
    "problemLevel": 5,
    "problemName": "ROT13",
    "average_try": 1.6376,
    "solvedtags": [
      {
        "bojTagId": 102,
        "key": "implementation"
      },
      {
        "bojTagId": 158,
        "key": "string"
      }
    ],
    "lastupdate": 1687116861.593256
  },
  "1259": {
    "problemId": "1259",
    "problemLevel": 5,
    "problemName": "팰린드롬수",
    "average_try": 1.7374,
    "solvedtags": [
      {
        "bojTagId": 102,
        "key": "implementation"
      },
      {
        "bojTagId": 158,
        "key": "string"
      }
    ],
    "lastupdate": 1687116861.593273
  },
  "9933": {
    "problemId": "9933",
    "problemLevel": 5,
    "problemName": "민균이의 비밀번호",
    "average_try": 2.4704,
    "solvedtags": [
      {
        "bojTagId": 175,
        "key": "data_structures"
      },
      {
        "bojTagId": 136,
        "key": "hash_set"
      },
      {
        "bojTagId": 102,
        "key": "implementation"
      },
      {
        "bojTagId": 158,
        "key": "string"
      }
    ],
    "lastupdate": 1687116861.593291
  },
  "6996": {
    "problemId": "6996",
    "problemLevel": 5,
    "problemName": "애너그램",
    "average_try": 1.9577,
    "solvedtags": [
      {
        "bojTagId": 102,
        "key": "implementation"
      },
      {
        "bojTagId": 97,
        "key": "sorting"
      },
      {
        "bojTagId": 158,
        "key": "string"
      }
    ],
    "lastupdate": 1687116861.593309
  },
  "20154": {
    "problemId": "20154",
    "problemLevel": 5,
    "problemName": "이 구역의 승자는 누구야?!",
    "average_try": 1.6013,
    "solvedtags": [
      {
        "bojTagId": 124,
        "key": "math"
      },
      {
        "bojTagId": 158,
        "key": "string"
      }
    ],
    "lastupdate": 1687116861.593326
  },
  "1316": {
    "problemId": "1316",
    "problemLevel": 6,
    "problemName": "그룹 단어 체커",
    "average_try": 1.9057,
    "solvedtags": [
      {
        "bojTagId": 102,
        "key": "implementation"
      },
      {
        "bojTagId": 158,
        "key": "string"
      }
    ],
    "lastupdate": 1687116861.593344
  },
  "2941": {
    "problemId": "2941",
    "problemLevel": 6,
    "problemName": "크로아티아 알파벳",
    "average_try": 2.2397,
    "solvedtags": [
      {
        "bojTagId": 102,
        "key": "implementation"
      },
      {
        "bojTagId": 158,
        "key": "string"
      }
    ],
    "lastupdate": 1687116861.593361
  },
  "1181": {
    "problemId": "1181",
    "problemLevel": 6,
    "problemName": "단어 정렬",
    "average_try": 2.4786,
    "solvedtags": [
      {
        "bojTagId": 97,
        "key": "sorting"
      },
      {
        "bojTagId": 158,
        "key": "string"
      }
    ],
    "lastupdate": 1687116861.593379
  },
  "3613": {
    "problemId": "3613",
    "problemLevel": 8,
    "problemName": "Java vs C++",
    "average_try": 4.9752,
    "solvedtags": [
      {
        "bojTagId": 137,
        "key": "case_work"
      },
      {
        "bojTagId": 102,
        "key": "implementation"
      },
      {
        "bojTagId": 96,
        "key": "parsing"
      },
      {
        "bojTagId": 158,
        "key": "string"
      }
    ],
    "lastupdate": 1687116861.593396
  },
  "9536": {
    "problemId": "9536",
    "problemLevel": 8,
    "problemName": "여우는 어떻게 울지?",
    "average_try": 2.3529,
    "solvedtags": [
      {
        "bojTagId": 96,
        "key": "parsing"
      },
      {
        "bojTagId": 158,
        "key": "string"
      }
    ],
    "lastupdate": 1687116861.593414
  },
  "14405": {
    "problemId": "14405",
    "problemLevel": 5,
    "problemName": "피카츄",
    "average_try": 2.0552,
    "solvedtags": [
      {
        "bojTagId": 158,
        "key": "string"
      }
    ],
    "lastupdate": 1687116861.593431
  },
  "4659": {
    "problemId": "4659",
    "problemLevel": 6,
    "problemName": "비밀번호 발음하기",
    "average_try": 2.0209,
    "solvedtags": [
      {
        "bojTagId": 102,
        "key": "implementation"
      },
      {
        "bojTagId": 158,
        "key": "string"
      }
    ],
    "lastupdate": 1687116861.593449
  },
  "16171": {
    "problemId": "16171",
    "problemLevel": 5,
    "problemName": "나는 친구가 적다 (Small)",
    "average_try": 1.9084,
    "solvedtags": [
      {
        "bojTagId": 158,
        "key": "string"
      }
    ],
    "lastupdate": 1687116861.593466
  },
  "12871": {
    "problemId": "12871",
    "problemLevel": 6,
    "problemName": "무한 문자열",
    "average_try": 2.8157,
    "solvedtags": [
      {
        "bojTagId": 102,
        "key": "implementation"
      },
      {
        "bojTagId": 124,
        "key": "math"
      },
      {
        "bojTagId": 158,
        "key": "string"
      }
    ],
    "lastupdate": 1687116861.593484
  },
  "2204": {
    "problemId": "2204",
    "problemLevel": 5,
    "problemName": "도비의 난독증 테스트",
    "average_try": 1.7915,
    "solvedtags": [
      {
        "bojTagId": 97,
        "key": "sorting"
      },
      {
        "bojTagId": 158,
        "key": "string"
      }
    ],
    "lastupdate": 1687116861.593502
  },
  "4446": {
    "problemId": "4446",
    "problemLevel": 6,
    "problemName": "ROT13",
    "average_try": 3.5474,
    "solvedtags": [
      {
        "bojTagId": 102,
        "key": "implementation"
      },
      {
        "bojTagId": 158,
        "key": "string"
      }
    ],
    "lastupdate": 1687116861.593519
  },
  "9342": {
    "problemId": "9342",
    "problemLevel": 8,
    "problemName": "염색체",
    "average_try": 1.443,
    "solvedtags": [
      {
        "bojTagId": 63,
        "key": "regex"
      },
      {
        "bojTagId": 158,
        "key": "string"
      }
    ],
    "lastupdate": 1687116861.593536
  },
  "20114": {
    "problemId": "20114",
    "problemLevel": 6,
    "problemName": "미아 노트",
    "average_try": 1.3293,
    "solvedtags": [
      {
        "bojTagId": 158,
        "key": "string"
      }
    ],
    "lastupdate": 1687116861.593554
  },
  "12933": {
    "problemId": "12933",
    "problemLevel": 8,
    "problemName": "오리",
    "average_try": 2.9048,
    "solvedtags": [
      {
        "bojTagId": 33,
        "key": "greedy"
      },
      {
        "bojTagId": 102,
        "key": "implementation"
      },
      {
        "bojTagId": 158,
        "key": "string"
      }
    ],
    "lastupdate": 1687116861.593572
  },
  "5534": {
    "problemId": "5534",
    "problemLevel": 7,
    "problemName": "간판",
    "average_try": 2.0184,
    "solvedtags": [
      {
        "bojTagId": 125,
        "key": "bruteforcing"
      },
      {
        "bojTagId": 102,
        "key": "implementation"
      },
      {
        "bojTagId": 158,
        "key": "string"
      }
    ],
    "lastupdate": 1687116861.593589
  },
  "6550": {
    "problemId": "6550",
    "problemLevel": 6,
    "problemName": "부분 문자열",
    "average_try": 2.6977,
    "solvedtags": [
      {
        "bojTagId": 33,
        "key": "greedy"
      },
      {
        "bojTagId": 158,
        "key": "string"
      }
    ],
    "lastupdate": 1687116861.593607
  },
  "4396": {
    "problemId": "4396",
    "problemLevel": 7,
    "problemName": "지뢰 찾기",
    "average_try": 3.3318,
    "solvedtags": [
      {
        "bojTagId": 102,
        "key": "implementation"
      }
    ],
    "lastupdate": 1687116861.593624
  },
  "9242": {
    "problemId": "9242",
    "problemLevel": 7,
    "problemName": "폭탄 해체",
    "average_try": 1.9943,
    "solvedtags": [
      {
        "bojTagId": 102,
        "key": "implementation"
      },
      {
        "bojTagId": 96,
        "key": "parsing"
      },
      {
        "bojTagId": 158,
        "key": "string"
      }
    ],
    "lastupdate": 1687116861.593642
  },
  "4836": {
    "problemId": "4836",
    "problemLevel": 7,
    "problemName": "춤",
    "average_try": 3.321,
    "solvedtags": [
      {
        "bojTagId": 102,
        "key": "implementation"
      },
      {
        "bojTagId": 96,
        "key": "parsing"
      },
      {
        "bojTagId": 158,
        "key": "string"
      }
    ],
    "lastupdate": 1687116861.593659
  },
  "1764": {
    "problemId": "1764",
    "problemLevel": 7,
    "problemName": "듣보잡",
    "average_try": 2.4604,
    "solvedtags": [
      {
        "bojTagId": 175,
        "key": "data_structures"
      },
      {
        "bojTagId": 136,
        "key": "hash_set"
      },
      {
        "bojTagId": 97,
        "key": "sorting"
      },
      {
        "bojTagId": 158,
        "key": "string"
      }
    ],
    "lastupdate": 1687116861.593676
  },
  "11656": {
    "problemId": "11656",
    "problemLevel": 7,
    "problemName": "접미사 배열",
    "average_try": 1.4229,
    "solvedtags": [
      {
        "bojTagId": 97,
        "key": "sorting"
      },
      {
        "bojTagId": 158,
        "key": "string"
      }
    ],
    "lastupdate": 1687116861.593694
  },
  "1620": {
    "problemId": "1620",
    "problemLevel": 7,
    "problemName": "나는야 포켓몬 마스터 이다솜",
    "average_try": 2.9513,
    "solvedtags": [
      {
        "bojTagId": 175,
        "key": "data_structures"
      },
      {
        "bojTagId": 136,
        "key": "hash_set"
      }
    ],
    "lastupdate": 1687116861.593711
  },
  "1213": {
    "problemId": "1213",
    "problemLevel": 8,
    "problemName": "팰린드롬 만들기",
    "average_try": 2.442,
    "solvedtags": [
      {
        "bojTagId": 33,
        "key": "greedy"
      },
      {
        "bojTagId": 102,
        "key": "implementation"
      },
      {
        "bojTagId": 158,
        "key": "string"
      }
    ],
    "lastupdate": 1687116861.593728
  },
  "20291": {
    "problemId": "20291",
    "problemLevel": 8,
    "problemName": "파일 정리",
    "average_try": 1.4887,
    "solvedtags": [
      {
        "bojTagId": 175,
        "key": "data_structures"
      },
      {
        "bojTagId": 136,
        "key": "hash_set"
      },
      {
        "bojTagId": 96,
        "key": "parsing"
      },
      {
        "bojTagId": 97,
        "key": "sorting"
      },
      {
        "bojTagId": 158,
        "key": "string"
      }
    ],
    "lastupdate": 1687116861.593758
  },
  "19844": {
    "problemId": "19844",
    "problemLevel": 7,
    "problemName": "단어 개수 세기",
    "average_try": 2.9658,
    "solvedtags": [
      {
        "bojTagId": 102,
        "key": "implementation"
      },
      {
        "bojTagId": 158,
        "key": "string"
      }
    ],
    "lastupdate": 1687116861.593776
  },
  "1622": {
    "problemId": "1622",
    "problemLevel": 7,
    "problemName": "공통 순열",
    "average_try": 4.1092,
    "solvedtags": [
      {
        "bojTagId": 97,
        "key": "sorting"
      },
      {
        "bojTagId": 158,
        "key": "string"
      }
    ],
    "lastupdate": 1687116861.593793
  },
  "17413": {
    "problemId": "17413",
    "problemLevel": 8,
    "problemName": "단어 뒤집기 2",
    "average_try": 1.7593,
    "solvedtags": [
      {
        "bojTagId": 175,
        "key": "data_structures"
      },
      {
        "bojTagId": 102,
        "key": "implementation"
      },
      {
        "bojTagId": 71,
        "key": "stack"
      },
      {
        "bojTagId": 158,
        "key": "string"
      }
    ],
    "lastupdate": 1687116861.593811
  },
  "11478": {
    "problemId": "11478",
    "problemLevel": 8,
    "problemName": "서로 다른 부분 문자열의 개수",
    "average_try": 1.606,
    "solvedtags": [
      {
        "bojTagId": 175,
        "key": "data_structures"
      },
      {
        "bojTagId": 136,
        "key": "hash_set"
      },
      {
        "bojTagId": 158,
        "key": "string"
      },
      {
        "bojTagId": 74,
        "key": "tree_set"
      }
    ],
    "lastupdate": 1687116861.593828
  },
  "2852": {
    "problemId": "2852",
    "problemLevel": 8,
    "problemName": "NBA 농구",
    "average_try": 2.4083,
    "solvedtags": [
      {
        "bojTagId": 102,
        "key": "implementation"
      },
      {
        "bojTagId": 158,
        "key": "string"
      }
    ],
    "lastupdate": 1687116861.593846
  },
  "1972": {
    "problemId": "1972",
    "problemLevel": 8,
    "problemName": "놀라운 문자열",
    "average_try": 1.6722,
    "solvedtags": [
      {
        "bojTagId": 175,
        "key": "data_structures"
      },
      {
        "bojTagId": 136,
        "key": "hash_set"
      },
      {
        "bojTagId": 102,
        "key": "implementation"
      },
      {
        "bojTagId": 158,
        "key": "string"
      }
    ],
    "lastupdate": 1687116861.593863
  },
  "19948": {
    "problemId": "19948",
    "problemLevel": 8,
    "problemName": "음유시인 영재",
    "average_try": 3.9234,
    "solvedtags": [
      {
        "bojTagId": 102,
        "key": "implementation"
      },
      {
        "bojTagId": 158,
        "key": "string"
      }
    ],
    "lastupdate": 1687116861.59388
  },
  "17609": {
    "problemId": "17609",
    "problemLevel": 11,
    "problemName": "회문",
    "average_try": 3.4775,
    "solvedtags": [
      {
        "bojTagId": 158,
        "key": "string"
      },
      {
        "bojTagId": 80,
        "key": "two_pointer"
      }
    ],
    "lastupdate": 1687116861.593898
  },
  "3005": {
    "problemId": "3005",
    "problemLevel": 9,
    "problemName": "크로스워드 퍼즐 쳐다보기",
    "average_try": 1.814,
    "solvedtags": [
      {
        "bojTagId": 102,
        "key": "implementation"
      },
      {
        "bojTagId": 96,
        "key": "parsing"
      },
      {
        "bojTagId": 97,
        "key": "sorting"
      },
      {
        "bojTagId": 158,
        "key": "string"
      }
    ],
    "lastupdate": 1687116861.593916
  },
  "19583": {
    "problemId": "19583",
    "problemLevel": 9,
    "problemName": "싸이버개강총회",
    "average_try": 2.5897,
    "solvedtags": [
      {
        "bojTagId": 175,
        "key": "data_structures"
      },
      {
        "bojTagId": 136,
        "key": "hash_set"
      },
      {
        "bojTagId": 102,
        "key": "implementation"
      },
      {
        "bojTagId": 158,
        "key": "string"
      }
    ],
    "lastupdate": 1687116861.593934
  },
  "13022": {
    "problemId": "13022",
    "problemLevel": 9,
    "problemName": "늑대와 올바른 단어",
    "average_try": 3.4413,
    "solvedtags": [
      {
        "bojTagId": 102,
        "key": "implementation"
      },
      {
        "bojTagId": 158,
        "key": "string"
      }
    ],
    "lastupdate": 1687116861.593951
  },
  "15927": {
    "problemId": "15927",
    "problemLevel": 11,
    "problemName": "회문은 회문아니야!!",
    "average_try": 2.4939,
    "solvedtags": [
      {
        "bojTagId": 109,
        "key": "ad_hoc"
      },
      {
        "bojTagId": 158,
        "key": "string"
      }
    ],
    "lastupdate": 1687116861.593968
  },
  "3107": {
    "problemId": "3107",
    "problemLevel": 11,
    "problemName": "IPv6",
    "average_try": 2.6765,
    "solvedtags": [
      {
        "bojTagId": 102,
        "key": "implementation"
      },
      {
        "bojTagId": 158,
        "key": "string"
      }
    ],
    "lastupdate": 1687116861.593985
  },
  "2671": {
    "problemId": "2671",
    "problemLevel": 11,
    "problemName": "잠수함식별",
    "average_try": 2.4717,
    "solvedtags": [
      {
        "bojTagId": 63,
        "key": "regex"
      },
      {
        "bojTagId": 158,
        "key": "string"
      }
    ],
    "lastupdate": 1687116861.594002
  },
  "20437": {
    "problemId": "20437",
    "problemLevel": 11,
    "problemName": "문자열 게임 2",
    "average_try": 2.4329,
    "solvedtags": [
      {
        "bojTagId": 68,
        "key": "sliding_window"
      },
      {
        "bojTagId": 158,
        "key": "string"
      }
    ],
    "lastupdate": 1687116861.594019
  },
  "16916": {
    "problemId": "16916",
    "problemLevel": 4,
    "problemName": "부분 문자열",
    "average_try": 2.6957,
    "solvedtags": [
      {
        "bojTagId": 158,
        "key": "string"
      },
      {
        "bojTagId": 102,
        "key": "implementation"
      }
    ],
    "lastupdate": 1687116861.594072
  },
  "2115": {
    "problemId": "2115",
    "problemLevel": 11,
    "problemName": "갤러리",
    "average_try": 1.3019,
    "solvedtags": [
      {
        "bojTagId": 102,
        "key": "implementation"
      }
    ],
    "lastupdate": 1687116861.594089
  },
  "16890": {
    "problemId": "16890",
    "problemLevel": 15,
    "problemName": "창업",
    "average_try": 5.9862,
    "solvedtags": [
      {
        "bojTagId": 140,
        "key": "game_theory"
      },
      {
        "bojTagId": 33,
        "key": "greedy"
      },
      {
        "bojTagId": 97,
        "key": "sorting"
      },
      {
        "bojTagId": 158,
        "key": "string"
      }
    ],
    "lastupdate": 1687116861.594107
  },
  "20210": {
    "problemId": "20210",
    "problemLevel": 14,
    "problemName": "파일 탐색기",
    "average_try": 4.2935,
    "solvedtags": [
      {
        "bojTagId": 102,
        "key": "implementation"
      },
      {
        "bojTagId": 97,
        "key": "sorting"
      },
      {
        "bojTagId": 158,
        "key": "string"
      }
    ],
    "lastupdate": 1687116861.594125
  },
  "14567": {
    "problemId": "14567",
    "problemLevel": 11,
    "problemName": "선수과목 (Prerequisite)",
    "average_try": 1.5212,
    "solvedtags": [
      {
        "bojTagId": 25,
        "key": "dp"
      },
      {
        "bojTagId": 7,
        "key": "graphs"
      },
      {
        "bojTagId": 78,
        "key": "topological_sorting"
      }
    ],
    "lastupdate": 1687116861.594772
  },
  "2056": {
    "problemId": "2056",
    "problemLevel": 12,
    "problemName": "작업",
    "average_try": 2.2855,
    "solvedtags": [
      {
        "bojTagId": 25,
        "key": "dp"
      },
      {
        "bojTagId": 7,
        "key": "graphs"
      },
      {
        "bojTagId": 78,
        "key": "topological_sorting"
      }
    ],
    "lastupdate": 1687116861.594796
  },
  "14676": {
    "problemId": "14676",
    "problemLevel": 13,
    "problemName": "영우는 사기꾼?",
    "average_try": 3.0994,
    "solvedtags": [
      {
        "bojTagId": 7,
        "key": "graphs"
      },
      {
        "bojTagId": 102,
        "key": "implementation"
      },
      {
        "bojTagId": 78,
        "key": "topological_sorting"
      }
    ],
    "lastupdate": 1687116861.594815
  },
  "1005": {
    "problemId": "1005",
    "problemLevel": 13,
    "problemName": "ACM Craft",
    "average_try": 3.6495,
    "solvedtags": [
      {
        "bojTagId": 25,
        "key": "dp"
      },
      {
        "bojTagId": 7,
        "key": "graphs"
      },
      {
        "bojTagId": 78,
        "key": "topological_sorting"
      }
    ],
    "lastupdate": 1687116861.594833
  },
  "1516": {
    "problemId": "1516",
    "problemLevel": 13,
    "problemName": "게임 개발",
    "average_try": 2.0589,
    "solvedtags": [
      {
        "bojTagId": 25,
        "key": "dp"
      },
      {
        "bojTagId": 7,
        "key": "graphs"
      },
      {
        "bojTagId": 78,
        "key": "topological_sorting"
      }
    ],
    "lastupdate": 1687116861.594851
  },
  "9470": {
    "problemId": "9470",
    "problemLevel": 13,
    "problemName": "Strahler 순서",
    "average_try": 2.5208,
    "solvedtags": [
      {
        "bojTagId": 7,
        "key": "graphs"
      },
      {
        "bojTagId": 78,
        "key": "topological_sorting"
      }
    ],
    "lastupdate": 1687116861.594869
  },
  "2252": {
    "problemId": "2252",
    "problemLevel": 13,
    "problemName": "줄 세우기",
    "average_try": 1.7665,
    "solvedtags": [
      {
        "bojTagId": 7,
        "key": "graphs"
      },
      {
        "bojTagId": 78,
        "key": "topological_sorting"
      }
    ],
    "lastupdate": 1687116861.594886
  },
  "1766": {
    "problemId": "1766",
    "problemLevel": 14,
    "problemName": "문제집",
    "average_try": 2.0677,
    "solvedtags": [
      {
        "bojTagId": 175,
        "key": "data_structures"
      },
      {
        "bojTagId": 7,
        "key": "graphs"
      },
      {
        "bojTagId": 59,
        "key": "priority_queue"
      },
      {
        "bojTagId": 78,
        "key": "topological_sorting"
      }
    ],
    "lastupdate": 1687116861.594918
  },
  "2623": {
    "problemId": "2623",
    "problemLevel": 13,
    "problemName": "음악프로그램",
    "average_try": 1.9795,
    "solvedtags": [
      {
        "bojTagId": 7,
        "key": "graphs"
      },
      {
        "bojTagId": 78,
        "key": "topological_sorting"
      }
    ],
    "lastupdate": 1687116861.594937
  },
  "2637": {
    "problemId": "2637",
    "problemLevel": 14,
    "problemName": "장난감 조립",
    "average_try": 2.0675,
    "solvedtags": [
      {
        "bojTagId": 25,
        "key": "dp"
      },
      {
        "bojTagId": 7,
        "key": "graphs"
      },
      {
        "bojTagId": 78,
        "key": "topological_sorting"
      }
    ],
    "lastupdate": 1687116861.594955
  },
  "20119": {
    "problemId": "20119",
    "problemLevel": 15,
    "problemName": "클레어와 물약",
    "average_try": 3.4121,
    "solvedtags": [
      {
        "bojTagId": 7,
        "key": "graphs"
      },
      {
        "bojTagId": 11,
        "key": "graph_traversal"
      },
      {
        "bojTagId": 78,
        "key": "topological_sorting"
      }
    ],
    "lastupdate": 1687116861.594974
  },
  "3665": {
    "problemId": "3665",
    "problemLevel": 15,
    "problemName": "최종 순위",
    "average_try": 2.6781,
    "solvedtags": [
      {
        "bojTagId": 7,
        "key": "graphs"
      },
      {
        "bojTagId": 78,
        "key": "topological_sorting"
      }
    ],
    "lastupdate": 1687116861.594991
  },
  "1948": {
    "problemId": "1948",
    "problemLevel": 16,
    "problemName": "임계경로",
    "average_try": 3.254,
    "solvedtags": [
      {
        "bojTagId": 7,
        "key": "graphs"
      },
      {
        "bojTagId": 11,
        "key": "graph_traversal"
      },
      {
        "bojTagId": 78,
        "key": "topological_sorting"
      }
    ],
    "lastupdate": 1687116861.595009
  },
  "1991": {
    "problemId": "1991",
    "problemLevel": 10,
    "problemName": "트리 순회",
    "average_try": 1.5045,
    "solvedtags": [
      {
        "bojTagId": 62,
        "key": "recursion"
      },
      {
        "bojTagId": 120,
        "key": "trees"
      }
    ],
    "lastupdate": 1687116861.595326
  },
  "9372": {
    "problemId": "9372",
    "problemLevel": 7,
    "problemName": "상근이의 여행",
    "average_try": 1.6541,
    "solvedtags": [
      {
        "bojTagId": 7,
        "key": "graphs"
      },
      {
        "bojTagId": 120,
        "key": "trees"
      }
    ],
    "lastupdate": 1687116861.59535
  },
  "9934": {
    "problemId": "9934",
    "problemLevel": 10,
    "problemName": "완전 이진 트리",
    "average_try": 1.4678,
    "solvedtags": [
      {
        "bojTagId": 62,
        "key": "recursion"
      },
      {
        "bojTagId": 120,
        "key": "trees"
      }
    ],
    "lastupdate": 1687116861.59537
  },
  "11725": {
    "problemId": "11725",
    "problemLevel": 9,
    "problemName": "트리의 부모 찾기",
    "average_try": 2.3679,
    "solvedtags": [
      {
        "bojTagId": 7,
        "key": "graphs"
      },
      {
        "bojTagId": 11,
        "key": "graph_traversal"
      },
      {
        "bojTagId": 120,
        "key": "trees"
      },
      {
        "bojTagId": 126,
        "key": "bfs"
      },
      {
        "bojTagId": 127,
        "key": "dfs"
      }
    ],
    "lastupdate": 1687116861.595398
  },
  "20364": {
    "problemId": "20364",
    "problemLevel": 10,
    "problemName": "부동산 다툼",
    "average_try": 3.2788,
    "solvedtags": [
      {
        "bojTagId": 120,
        "key": "trees"
      }
    ],
    "lastupdate": 1687116861.595416
  },
  "1068": {
    "problemId": "1068",
    "problemLevel": 11,
    "problemName": "트리",
    "average_try": 3.5416,
    "solvedtags": [
      {
        "bojTagId": 127,
        "key": "dfs"
      },
      {
        "bojTagId": 7,
        "key": "graphs"
      },
      {
        "bojTagId": 11,
        "key": "graph_traversal"
      },
      {
        "bojTagId": 120,
        "key": "trees"
      }
    ],
    "lastupdate": 1687116861.595434
  },
  "5639": {
    "problemId": "5639",
    "problemLevel": 11,
    "problemName": "이진 검색 트리",
    "average_try": 2.6246,
    "solvedtags": [
      {
        "bojTagId": 7,
        "key": "graphs"
      },
      {
        "bojTagId": 11,
        "key": "graph_traversal"
      },
      {
        "bojTagId": 62,
        "key": "recursion"
      },
      {
        "bojTagId": 120,
        "key": "trees"
      }
    ],
    "lastupdate": 1687116861.595452
  },
  "15900": {
    "problemId": "15900",
    "problemLevel": 10,
    "problemName": "나무 탈출",
    "average_try": 2.6389,
    "solvedtags": [
      {
        "bojTagId": 127,
        "key": "dfs"
      },
      {
        "bojTagId": 7,
        "key": "graphs"
      },
      {
        "bojTagId": 11,
        "key": "graph_traversal"
      },
      {
        "bojTagId": 120,
        "key": "trees"
      }
    ],
    "lastupdate": 1687116861.595469
  },
  "6416": {
    "problemId": "6416",
    "problemLevel": 0,
    "problemName": "트리인가?",
    "average_try": 5.044,
    "solvedtags": [
      {
        "bojTagId": 120,
        "key": "trees"
      },
      {
        "bojTagId": 7,
        "key": "graphs"
      },
      {
        "bojTagId": 175,
        "key": "data_structures"
      }
    ],
    "lastupdate": 1687116861.595487
  },
  "14675": {
    "problemId": "14675",
    "problemLevel": 10,
    "problemName": "단절점과 단절선",
    "average_try": 1.9695,
    "solvedtags": [
      {
        "bojTagId": 4,
        "key": "articulation"
      },
      {
        "bojTagId": 7,
        "key": "graphs"
      },
      {
        "bojTagId": 120,
        "key": "trees"
      }
    ],
    "lastupdate": 1687116861.595504
  },
  "15681": {
    "problemId": "15681",
    "problemLevel": 11,
    "problemName": "트리와 쿼리",
    "average_try": 2.1686,
    "solvedtags": [
      {
        "bojTagId": 127,
        "key": "dfs"
      },
      {
        "bojTagId": 25,
        "key": "dp"
      },
      {
        "bojTagId": 92,
        "key": "dp_tree"
      },
      {
        "bojTagId": 7,
        "key": "graphs"
      },
      {
        "bojTagId": 11,
        "key": "graph_traversal"
      },
      {
        "bojTagId": 120,
        "key": "trees"
      }
    ],
    "lastupdate": 1687116861.595522
  },
  "17073": {
    "problemId": "17073",
    "problemLevel": 11,
    "problemName": "나무 위의 빗물",
    "average_try": 2.6594,
    "solvedtags": [
      {
        "bojTagId": 7,
        "key": "graphs"
      },
      {
        "bojTagId": 11,
        "key": "graph_traversal"
      },
      {
        "bojTagId": 124,
        "key": "math"
      },
      {
        "bojTagId": 120,
        "key": "trees"
      }
    ],
    "lastupdate": 1687116861.595539
  },
  "19641": {
    "problemId": "19641",
    "problemLevel": 11,
    "problemName": "중첩 집합 모델",
    "average_try": 2.5606,
    "solvedtags": [
      {
        "bojTagId": 127,
        "key": "dfs"
      },
      {
        "bojTagId": 150,
        "key": "euler_tour_technique"
      },
      {
        "bojTagId": 7,
        "key": "graphs"
      },
      {
        "bojTagId": 11,
        "key": "graph_traversal"
      },
      {
        "bojTagId": 120,
        "key": "trees"
      }
    ],
    "lastupdate": 1687116861.595556
  },
  "1240": {
    "problemId": "1240",
    "problemLevel": 11,
    "problemName": "노드사이의 거리",
    "average_try": 1.8807,
    "solvedtags": [
      {
        "bojTagId": 126,
        "key": "bfs"
      },
      {
        "bojTagId": 127,
        "key": "dfs"
      },
      {
        "bojTagId": 7,
        "key": "graphs"
      },
      {
        "bojTagId": 11,
        "key": "graph_traversal"
      },
      {
        "bojTagId": 120,
        "key": "trees"
      }
    ],
    "lastupdate": 1687116861.595574
  },
  "1967": {
    "problemId": "1967",
    "problemLevel": 12,
    "problemName": "트리의 지름",
    "average_try": 2.4215,
    "solvedtags": [
      {
        "bojTagId": 127,
        "key": "dfs"
      },
      {
        "bojTagId": 7,
        "key": "graphs"
      },
      {
        "bojTagId": 11,
        "key": "graph_traversal"
      },
      {
        "bojTagId": 120,
        "key": "trees"
      }
    ],
    "lastupdate": 1687116861.595591
  },
  "3584": {
    "problemId": "3584",
    "problemLevel": 12,
    "problemName": "가장 가까운 공통 조상",
    "average_try": 1.9408,
    "solvedtags": [
      {
        "bojTagId": 127,
        "key": "dfs"
      },
      {
        "bojTagId": 7,
        "key": "graphs"
      },
      {
        "bojTagId": 11,
        "key": "graph_traversal"
      },
      {
        "bojTagId": 41,
        "key": "lca"
      },
      {
        "bojTagId": 120,
        "key": "trees"
      }
    ],
    "lastupdate": 1687116861.595609
  },
  "4256": {
    "problemId": "4256",
    "problemLevel": 14,
    "problemName": "트리",
    "average_try": 1.7857,
    "solvedtags": [
      {
        "bojTagId": 24,
        "key": "divide_and_conquer"
      },
      {
        "bojTagId": 62,
        "key": "recursion"
      },
      {
        "bojTagId": 120,
        "key": "trees"
      }
    ],
    "lastupdate": 1687116861.595627
  },
  "4803": {
    "problemId": "4803",
    "problemLevel": 12,
    "problemName": "트리",
    "average_try": 3.1656,
    "solvedtags": [
      {
        "bojTagId": 175,
        "key": "data_structures"
      },
      {
        "bojTagId": 127,
        "key": "dfs"
      },
      {
        "bojTagId": 81,
        "key": "disjoint_set"
      },
      {
        "bojTagId": 7,
        "key": "graphs"
      },
      {
        "bojTagId": 11,
        "key": "graph_traversal"
      },
      {
        "bojTagId": 120,
        "key": "trees"
      }
    ],
    "lastupdate": 1687116861.595644
  },
  "4933": {
    "problemId": "4933",
    "problemLevel": 14,
    "problemName": "뉴턴의 사과",
    "average_try": 2.9811,
    "solvedtags": [
      {
        "bojTagId": 175,
        "key": "data_structures"
      },
      {
        "bojTagId": 71,
        "key": "stack"
      },
      {
        "bojTagId": 120,
        "key": "trees"
      }
    ],
    "lastupdate": 1687116861.595662
  },
  "9489": {
    "problemId": "9489",
    "problemLevel": 12,
    "problemName": "사촌",
    "average_try": 3.5519,
    "solvedtags": [
      {
        "bojTagId": 175,
        "key": "data_structures"
      },
      {
        "bojTagId": 120,
        "key": "trees"
      }
    ],
    "lastupdate": 1687116861.595679
  },
  "14267": {
    "problemId": "14267",
    "problemLevel": 12,
    "problemName": "회사 문화 1",
    "average_try": 2.7561,
    "solvedtags": [
      {
        "bojTagId": 127,
        "key": "dfs"
      },
      {
        "bojTagId": 25,
        "key": "dp"
      },
      {
        "bojTagId": 92,
        "key": "dp_tree"
      },
      {
        "bojTagId": 7,
        "key": "graphs"
      },
      {
        "bojTagId": 11,
        "key": "graph_traversal"
      },
      {
        "bojTagId": 120,
        "key": "trees"
      }
    ],
    "lastupdate": 1687116861.595696
  },
  "19542": {
    "problemId": "19542",
    "problemLevel": 13,
    "problemName": "전단지 돌리기",
    "average_try": 2.5327,
    "solvedtags": [
      {
        "bojTagId": 127,
        "key": "dfs"
      },
      {
        "bojTagId": 7,
        "key": "graphs"
      },
      {
        "bojTagId": 11,
        "key": "graph_traversal"
      },
      {
        "bojTagId": 120,
        "key": "trees"
      }
    ],
    "lastupdate": 1687116861.595713
  },
  "20924": {
    "problemId": "20924",
    "problemLevel": 11,
    "problemName": "트리의 기둥과 가지",
    "average_try": 3.1155,
    "solvedtags": [
      {
        "bojTagId": 127,
        "key": "dfs"
      },
      {
        "bojTagId": 7,
        "key": "graphs"
      },
      {
        "bojTagId": 11,
        "key": "graph_traversal"
      },
      {
        "bojTagId": 120,
        "key": "trees"
      }
    ],
    "lastupdate": 1687116861.59573
  },
  "20955": {
    "problemId": "20955",
    "problemLevel": 12,
    "problemName": "민서의 응급 수술",
    "average_try": 2.7477,
    "solvedtags": [
      {
        "bojTagId": 175,
        "key": "data_structures"
      },
      {
        "bojTagId": 81,
        "key": "disjoint_set"
      },
      {
        "bojTagId": 7,
        "key": "graphs"
      },
      {
        "bojTagId": 120,
        "key": "trees"
      }
    ],
    "lastupdate": 1687116861.595748
  },
  "21276": {
    "problemId": "21276",
    "problemLevel": 14,
    "problemName": "계보 복원가 호석",
    "average_try": 2.0405,
    "solvedtags": [
      {
        "bojTagId": 175,
        "key": "data_structures"
      },
      {
        "bojTagId": 7,
        "key": "graphs"
      },
      {
        "bojTagId": 136,
        "key": "hash_set"
      },
      {
        "bojTagId": 97,
        "key": "sorting"
      },
      {
        "bojTagId": 78,
        "key": "topological_sorting"
      },
      {
        "bojTagId": 120,
        "key": "trees"
      }
    ],
    "lastupdate": 1687116861.595765
  },
  "1167": {
    "problemId": "1167",
    "problemLevel": 14,
    "problemName": "트리의 지름",
    "average_try": 2.9519,
    "solvedtags": [
      {
        "bojTagId": 127,
        "key": "dfs"
      },
      {
        "bojTagId": 7,
        "key": "graphs"
      },
      {
        "bojTagId": 11,
        "key": "graph_traversal"
      },
      {
        "bojTagId": 120,
        "key": "trees"
      }
    ],
    "lastupdate": 1687116861.595782
  },
  "1595": {
    "problemId": "1595",
    "problemLevel": 12,
    "problemName": "북쪽나라의 도로",
    "average_try": 2.9103,
    "solvedtags": [
      {
        "bojTagId": 127,
        "key": "dfs"
      },
      {
        "bojTagId": 7,
        "key": "graphs"
      },
      {
        "bojTagId": 11,
        "key": "graph_traversal"
      },
      {
        "bojTagId": 120,
        "key": "trees"
      }
    ],
    "lastupdate": 1687116861.595799
  },
  "2058": {
    "problemId": "2058",
    "problemLevel": 13,
    "problemName": "원자의 에너지",
    "average_try": 3.5714,
    "solvedtags": [
      {
        "bojTagId": 25,
        "key": "dp"
      },
      {
        "bojTagId": 92,
        "key": "dp_tree"
      },
      {
        "bojTagId": 120,
        "key": "trees"
      }
    ],
    "lastupdate": 1687116861.595816
  },
  "2263": {
    "problemId": "2263",
    "problemLevel": 15,
    "problemName": "트리의 순회",
    "average_try": 3.0729,
    "solvedtags": [
      {
        "bojTagId": 24,
        "key": "divide_and_conquer"
      },
      {
        "bojTagId": 62,
        "key": "recursion"
      },
      {
        "bojTagId": 120,
        "key": "trees"
      }
    ],
    "lastupdate": 1687116861.595833
  },
  "2533": {
    "problemId": "2533",
    "problemLevel": 13,
    "problemName": "사회망 서비스(SNS)",
    "average_try": 2.7288,
    "solvedtags": [
      {
        "bojTagId": 25,
        "key": "dp"
      },
      {
        "bojTagId": 92,
        "key": "dp_tree"
      },
      {
        "bojTagId": 120,
        "key": "trees"
      }
    ],
    "lastupdate": 1687116861.59585
  },
  "11437": {
    "problemId": "11437",
    "problemLevel": 13,
    "problemName": "LCA",
    "average_try": 2.4387,
    "solvedtags": [
      {
        "bojTagId": 7,
        "key": "graphs"
      },
      {
        "bojTagId": 41,
        "key": "lca"
      },
      {
        "bojTagId": 120,
        "key": "trees"
      }
    ],
    "lastupdate": 1687116861.595866
  },
  "12896": {
    "problemId": "12896",
    "problemLevel": 14,
    "problemName": "스크루지 민호",
    "average_try": 2.8176,
    "solvedtags": [
      {
        "bojTagId": 127,
        "key": "dfs"
      },
      {
        "bojTagId": 7,
        "key": "graphs"
      },
      {
        "bojTagId": 11,
        "key": "graph_traversal"
      },
      {
        "bojTagId": 120,
        "key": "trees"
      }
    ],
    "lastupdate": 1687116861.595884
  },
  "19535": {
    "problemId": "19535",
    "problemLevel": 13,
    "problemName": "ㄷㄷㄷㅈ",
    "average_try": 3.4649,
    "solvedtags": [
      {
        "bojTagId": 6,
        "key": "combinatorics"
      },
      {
        "bojTagId": 124,
        "key": "math"
      },
      {
        "bojTagId": 120,
        "key": "trees"
      }
    ],
    "lastupdate": 1687116861.595901
  },
  "2250": {
    "problemId": "2250",
    "problemLevel": 14,
    "problemName": "트리의 높이와 너비",
    "average_try": 3.6099,
    "solvedtags": [
      {
        "bojTagId": 127,
        "key": "dfs"
      },
      {
        "bojTagId": 7,
        "key": "graphs"
      },
      {
        "bojTagId": 11,
        "key": "graph_traversal"
      },
      {
        "bojTagId": 120,
        "key": "trees"
      }
    ],
    "lastupdate": 1687116861.595918
  },
  "4315": {
    "problemId": "4315",
    "problemLevel": 16,
    "problemName": "나무 위의 구슬",
    "average_try": 2.3284,
    "solvedtags": [
      {
        "bojTagId": 127,
        "key": "dfs"
      },
      {
        "bojTagId": 25,
        "key": "dp"
      },
      {
        "bojTagId": 92,
        "key": "dp_tree"
      },
      {
        "bojTagId": 7,
        "key": "graphs"
      },
      {
        "bojTagId": 11,
        "key": "graph_traversal"
      },
      {
        "bojTagId": 120,
        "key": "trees"
      }
    ],
    "lastupdate": 1687116861.595935
  },
  "14657": {
    "problemId": "14657",
    "problemLevel": 14,
    "problemName": "준오는 최종인재야!!",
    "average_try": 3.7552,
    "solvedtags": [
      {
        "bojTagId": 127,
        "key": "dfs"
      },
      {
        "bojTagId": 7,
        "key": "graphs"
      },
      {
        "bojTagId": 11,
        "key": "graph_traversal"
      },
      {
        "bojTagId": 120,
        "key": "trees"
      }
    ],
    "lastupdate": 1687116861.595953
  },
  "16437": {
    "problemId": "16437",
    "problemLevel": 13,
    "problemName": "양 구출 작전",
    "average_try": 3.7406,
    "solvedtags": [
      {
        "bojTagId": 127,
        "key": "dfs"
      },
      {
        "bojTagId": 7,
        "key": "graphs"
      },
      {
        "bojTagId": 11,
        "key": "graph_traversal"
      },
      {
        "bojTagId": 120,
        "key": "trees"
      }
    ],
    "lastupdate": 1687116861.59597
  },
  "1949": {
    "problemId": "1949",
    "problemLevel": 14,
    "problemName": "우수 마을",
    "average_try": 1.884,
    "solvedtags": [
      {
        "bojTagId": 25,
        "key": "dp"
      },
      {
        "bojTagId": 92,
        "key": "dp_tree"
      },
      {
        "bojTagId": 120,
        "key": "trees"
      }
    ],
    "lastupdate": 1687116861.595987
  },
  "2213": {
    "problemId": "2213",
    "problemLevel": 15,
    "problemName": "트리의 독립집합",
    "average_try": 2.0991,
    "solvedtags": [
      {
        "bojTagId": 25,
        "key": "dp"
      },
      {
        "bojTagId": 92,
        "key": "dp_tree"
      },
      {
        "bojTagId": 120,
        "key": "trees"
      }
    ],
    "lastupdate": 1687116861.596004
  },
  "2233": {
    "problemId": "2233",
    "problemLevel": 14,
    "problemName": "사과나무",
    "average_try": 3.0623,
    "solvedtags": [
      {
        "bojTagId": 175,
        "key": "data_structures"
      },
      {
        "bojTagId": 7,
        "key": "graphs"
      },
      {
        "bojTagId": 11,
        "key": "graph_traversal"
      },
      {
        "bojTagId": 41,
        "key": "lca"
      },
      {
        "bojTagId": 71,
        "key": "stack"
      },
      {
        "bojTagId": 120,
        "key": "trees"
      }
    ],
    "lastupdate": 1687116861.596021
  },
  "12912": {
    "problemId": "12912",
    "problemLevel": 15,
    "problemName": "트리 수정",
    "average_try": 2.1268,
    "solvedtags": [
      {
        "bojTagId": 125,
        "key": "bruteforcing"
      },
      {
        "bojTagId": 127,
        "key": "dfs"
      },
      {
        "bojTagId": 7,
        "key": "graphs"
      },
      {
        "bojTagId": 11,
        "key": "graph_traversal"
      },
      {
        "bojTagId": 120,
        "key": "trees"
      }
    ],
    "lastupdate": 1687116861.596038
  },
  "12978": {
    "problemId": "12978",
    "problemLevel": 13,
    "problemName": "스크루지 민호 2",
    "average_try": 2.3088,
    "solvedtags": [
      {
        "bojTagId": 25,
        "key": "dp"
      },
      {
        "bojTagId": 92,
        "key": "dp_tree"
      },
      {
        "bojTagId": 120,
        "key": "trees"
      }
    ],
    "lastupdate": 1687116861.596056
  },
  "14570": {
    "problemId": "14570",
    "problemLevel": 14,
    "problemName": "나무 위의 구슬",
    "average_try": 3.3094,
    "solvedtags": [
      {
        "bojTagId": 127,
        "key": "dfs"
      },
      {
        "bojTagId": 7,
        "key": "graphs"
      },
      {
        "bojTagId": 11,
        "key": "graph_traversal"
      },
      {
        "bojTagId": 120,
        "key": "trees"
      }
    ],
    "lastupdate": 1687116861.596074
  },
  "19581": {
    "problemId": "19581",
    "problemLevel": 15,
    "problemName": "두 번째 트리의 지름",
    "average_try": 2.3817,
    "solvedtags": [
      {
        "bojTagId": 127,
        "key": "dfs"
      },
      {
        "bojTagId": 7,
        "key": "graphs"
      },
      {
        "bojTagId": 11,
        "key": "graph_traversal"
      },
      {
        "bojTagId": 120,
        "key": "trees"
      }
    ],
    "lastupdate": 1687116861.596091
  },
  "14425": {
    "problemId": "14425",
    "problemLevel": 8,
    "problemName": "문자열 집합",
    "average_try": 1.8576,
    "solvedtags": [
      {
        "bojTagId": 175,
        "key": "data_structures"
      },
      {
        "bojTagId": 136,
        "key": "hash_set"
      },
      {
        "bojTagId": 158,
        "key": "string"
      },
      {
        "bojTagId": 74,
        "key": "tree_set"
      }
    ],
    "lastupdate": 1687116861.596607
  },
  "5052": {
    "problemId": "5052",
    "problemLevel": 12,
    "problemName": "전화번호 목록",
    "average_try": 3.3724,
    "solvedtags": [
      {
        "bojTagId": 175,
        "key": "data_structures"
      },
      {
        "bojTagId": 97,
        "key": "sorting"
      },
      {
        "bojTagId": 158,
        "key": "string"
      },
      {
        "bojTagId": 120,
        "key": "trees"
      },
      {
        "bojTagId": 79,
        "key": "trie"
      }
    ],
    "lastupdate": 1687116861.596632
  },
  "4358": {
    "problemId": "4358",
    "problemLevel": 9,
    "problemName": "생태학",
    "average_try": 2.7633,
    "solvedtags": [
      {
        "bojTagId": 175,
        "key": "data_structures"
      },
      {
        "bojTagId": 136,
        "key": "hash_set"
      },
      {
        "bojTagId": 158,
        "key": "string"
      },
      {
        "bojTagId": 74,
        "key": "tree_set"
      }
    ],
    "lastupdate": 1687116861.596652
  },
  "14725": {
    "problemId": "14725",
    "problemLevel": 13,
    "problemName": "개미굴",
    "average_try": 1.5152,
    "solvedtags": [
      {
        "bojTagId": 175,
        "key": "data_structures"
      },
      {
        "bojTagId": 158,
        "key": "string"
      },
      {
        "bojTagId": 120,
        "key": "trees"
      },
      {
        "bojTagId": 79,
        "key": "trie"
      }
    ],
    "lastupdate": 1687116861.59668
  },
  "20166": {
    "problemId": "20166",
    "problemLevel": 11,
    "problemName": "문자열 지옥에 빠진 호석",
    "average_try": 2.8841,
    "solvedtags": [
      {
        "bojTagId": 175,
        "key": "data_structures"
      },
      {
        "bojTagId": 127,
        "key": "dfs"
      },
      {
        "bojTagId": 25,
        "key": "dp"
      },
      {
        "bojTagId": 7,
        "key": "graphs"
      },
      {
        "bojTagId": 11,
        "key": "graph_traversal"
      },
      {
        "bojTagId": 136,
        "key": "hash_set"
      }
    ],
    "lastupdate": 1687116861.596699
  },
  "9202": {
    "problemId": "9202",
    "problemLevel": 16,
    "problemName": "Boggle",
    "average_try": 3.8935,
    "solvedtags": [
      {
        "bojTagId": 5,
        "key": "backtracking"
      },
      {
        "bojTagId": 125,
        "key": "bruteforcing"
      },
      {
        "bojTagId": 175,
        "key": "data_structures"
      },
      {
        "bojTagId": 127,
        "key": "dfs"
      },
      {
        "bojTagId": 7,
        "key": "graphs"
      },
      {
        "bojTagId": 11,
        "key": "graph_traversal"
      },
      {
        "bojTagId": 158,
        "key": "string"
      },
      {
        "bojTagId": 120,
        "key": "trees"
      },
      {
        "bojTagId": 79,
        "key": "trie"
      }
    ],
    "lastupdate": 1687116861.596717
  },
  "5670": {
    "problemId": "5670",
    "problemLevel": 17,
    "problemName": "휴대폰 자판",
    "average_try": 3.1235,
    "solvedtags": [
      {
        "bojTagId": 175,
        "key": "data_structures"
      },
      {
        "bojTagId": 158,
        "key": "string"
      },
      {
        "bojTagId": 120,
        "key": "trees"
      },
      {
        "bojTagId": 79,
        "key": "trie"
      }
    ],
    "lastupdate": 1687116861.596734
  },
  "5446": {
    "problemId": "5446",
    "problemLevel": 18,
    "problemName": "용량 부족",
    "average_try": 2.7788,
    "solvedtags": [
      {
        "bojTagId": 175,
        "key": "data_structures"
      },
      {
        "bojTagId": 158,
        "key": "string"
      },
      {
        "bojTagId": 120,
        "key": "trees"
      },
      {
        "bojTagId": 79,
        "key": "trie"
      }
    ],
    "lastupdate": 1687116861.596751
  },
  "19585": {
    "problemId": "19585",
    "problemLevel": 18,
    "problemName": "전설",
    "average_try": 7.8822,
    "solvedtags": [
      {
        "bojTagId": 175,
        "key": "data_structures"
      },
      {
        "bojTagId": 8,
        "key": "hashing"
      },
      {
        "bojTagId": 158,
        "key": "string"
      },
      {
        "bojTagId": 120,
        "key": "trees"
      },
      {
        "bojTagId": 79,
        "key": "trie"
      }
    ],
    "lastupdate": 1687116861.596769
  },
  "2470": {
    "problemId": "2470",
    "problemLevel": 11,
    "problemName": "두 용액",
    "average_try": 3.2921,
    "solvedtags": [
      {
        "bojTagId": 12,
        "key": "binary_search"
      },
      {
        "bojTagId": 97,
        "key": "sorting"
      },
      {
        "bojTagId": 80,
        "key": "two_pointer"
      }
    ],
    "lastupdate": 1687116861.597026
  },
  "15961": {
    "problemId": "15961",
    "problemLevel": 12,
    "problemName": "회전 초밥",
    "average_try": 2.6899,
    "solvedtags": [
      {
        "bojTagId": 68,
        "key": "sliding_window"
      },
      {
        "bojTagId": 80,
        "key": "two_pointer"
      }
    ],
    "lastupdate": 1687116861.59705
  },
  "1806": {
    "problemId": "1806",
    "problemLevel": 12,
    "problemName": "부분합",
    "average_try": 3.9225,
    "solvedtags": [
      {
        "bojTagId": 139,
        "key": "prefix_sum"
      },
      {
        "bojTagId": 80,
        "key": "two_pointer"
      }
    ],
    "lastupdate": 1687116861.597071
  },
  "7453": {
    "problemId": "7453",
    "problemLevel": 14,
    "problemName": "합이 0인 네 정수",
    "average_try": 4.4288,
    "solvedtags": [
      {
        "bojTagId": 12,
        "key": "binary_search"
      },
      {
        "bojTagId": 46,
        "key": "mitm"
      },
      {
        "bojTagId": 97,
        "key": "sorting"
      },
      {
        "bojTagId": 80,
        "key": "two_pointer"
      }
    ],
    "lastupdate": 1687116861.59709
  },
  "15565": {
    "problemId": "15565",
    "problemLevel": 10,
    "problemName": "귀여운 라이언",
    "average_try": 2.6523,
    "solvedtags": [
      {
        "bojTagId": 68,
        "key": "sliding_window"
      },
      {
        "bojTagId": 80,
        "key": "two_pointer"
      }
    ],
    "lastupdate": 1687116861.597108
  },
  "2467": {
    "problemId": "2467",
    "problemLevel": 11,
    "problemName": "용액",
    "average_try": 2.7264,
    "solvedtags": [
      {
        "bojTagId": 12,
        "key": "binary_search"
      },
      {
        "bojTagId": 80,
        "key": "two_pointer"
      }
    ],
    "lastupdate": 1687116861.597128
  },
  "2473": {
    "problemId": "2473",
    "problemLevel": 13,
    "problemName": "세 용액",
    "average_try": 3.7588,
    "solvedtags": [
      {
        "bojTagId": 12,
        "key": "binary_search"
      },
      {
        "bojTagId": 97,
        "key": "sorting"
      },
      {
        "bojTagId": 80,
        "key": "two_pointer"
      }
    ],
    "lastupdate": 1687116861.597146
  },
  "1644": {
    "problemId": "1644",
    "problemLevel": 13,
    "problemName": "소수의 연속합",
    "average_try": 2.4175,
    "solvedtags": [
      {
        "bojTagId": 124,
        "key": "math"
      },
      {
        "bojTagId": 95,
        "key": "number_theory"
      },
      {
        "bojTagId": 9,
        "key": "primality_test"
      },
      {
        "bojTagId": 67,
        "key": "sieve"
      },
      {
        "bojTagId": 80,
        "key": "two_pointer"
      }
    ],
    "lastupdate": 1687116861.597164
  },
  "20181": {
    "problemId": "20181",
    "problemLevel": 14,
    "problemName": "꿈틀꿈틀 호석 애벌레 - 효율성",
    "average_try": 2.4667,
    "solvedtags": [
      {
        "bojTagId": 12,
        "key": "binary_search"
      },
      {
        "bojTagId": 25,
        "key": "dp"
      },
      {
        "bojTagId": 139,
        "key": "prefix_sum"
      },
      {
        "bojTagId": 80,
        "key": "two_pointer"
      }
    ],
    "lastupdate": 1687116861.597182
  },
  "16472": {
    "problemId": "16472",
    "problemLevel": 12,
    "problemName": "고냥이",
    "average_try": 2.5217,
    "solvedtags": [
      {
        "bojTagId": 80,
        "key": "two_pointer"
      }
    ],
    "lastupdate": 1687116861.5972
  },
  "11728": {
    "problemId": "11728",
    "problemLevel": 6,
    "problemName": "배열 합치기",
    "average_try": 2.1843,
    "solvedtags": [
      {
        "bojTagId": 97,
        "key": "sorting"
      },
      {
        "bojTagId": 80,
        "key": "two_pointer"
      }
    ],
    "lastupdate": 1687116861.597217
  },
  "2018": {
    "problemId": "2018",
    "problemLevel": 6,
    "problemName": "수들의 합 5",
    "average_try": 2.0362,
    "solvedtags": [
      {
        "bojTagId": 124,
        "key": "math"
      },
      {
        "bojTagId": 80,
        "key": "two_pointer"
      }
    ],
    "lastupdate": 1687116861.597234
  },
  "1940": {
    "problemId": "1940",
    "problemLevel": 7,
    "problemName": "주몽",
    "average_try": 2.1211,
    "solvedtags": [
      {
        "bojTagId": 97,
        "key": "sorting"
      },
      {
        "bojTagId": 80,
        "key": "two_pointer"
      }
    ],
    "lastupdate": 1687116861.597252
  },
  "3273": {
    "problemId": "3273",
    "problemLevel": 8,
    "problemName": "두 수의 합",
    "average_try": 2.8604,
    "solvedtags": [
      {
        "bojTagId": 97,
        "key": "sorting"
      },
      {
        "bojTagId": 80,
        "key": "two_pointer"
      }
    ],
    "lastupdate": 1687116861.597269
  },
  "10025": {
    "problemId": "10025",
    "problemLevel": 8,
    "problemName": "게으른 백곰",
    "average_try": 3.3652,
    "solvedtags": [
      {
        "bojTagId": 139,
        "key": "prefix_sum"
      },
      {
        "bojTagId": 68,
        "key": "sliding_window"
      },
      {
        "bojTagId": 80,
        "key": "two_pointer"
      }
    ],
    "lastupdate": 1687116861.597286
  },
  "6159": {
    "problemId": "6159",
    "problemLevel": 6,
    "problemName": "Costume Party",
    "average_try": 1.7922,
    "solvedtags": [
      {
        "bojTagId": 125,
        "key": "bruteforcing"
      },
      {
        "bojTagId": 97,
        "key": "sorting"
      },
      {
        "bojTagId": 80,
        "key": "two_pointer"
      }
    ],
    "lastupdate": 1687116861.597304
  },
  "2003": {
    "problemId": "2003",
    "problemLevel": 7,
    "problemName": "수들의 합 2",
    "average_try": 2.073,
    "solvedtags": [
      {
        "bojTagId": 125,
        "key": "bruteforcing"
      },
      {
        "bojTagId": 139,
        "key": "prefix_sum"
      },
      {
        "bojTagId": 80,
        "key": "two_pointer"
      }
    ],
    "lastupdate": 1687116861.597321
  },
  "2559": {
    "problemId": "2559",
    "problemLevel": 8,
    "problemName": "수열",
    "average_try": 2.7819,
    "solvedtags": [
      {
        "bojTagId": 139,
        "key": "prefix_sum"
      },
      {
        "bojTagId": 68,
        "key": "sliding_window"
      },
      {
        "bojTagId": 80,
        "key": "two_pointer"
      }
    ],
    "lastupdate": 1687116861.597339
  },
  "2531": {
    "problemId": "2531",
    "problemLevel": 10,
    "problemName": "회전 초밥",
    "average_try": 2.6437,
    "solvedtags": [
      {
        "bojTagId": 125,
        "key": "bruteforcing"
      },
      {
        "bojTagId": 80,
        "key": "two_pointer"
      }
    ],
    "lastupdate": 1687116861.597356
  },
  "2118": {
    "problemId": "2118",
    "problemLevel": 11,
    "problemName": "두 개의 탑",
    "average_try": 2.4652,
    "solvedtags": [
      {
        "bojTagId": 139,
        "key": "prefix_sum"
      },
      {
        "bojTagId": 80,
        "key": "two_pointer"
      }
    ],
    "lastupdate": 1687116861.597374
  },
  "20922": {
    "problemId": "20922",
    "problemLevel": 10,
    "problemName": "겹치는 건 싫어",
    "average_try": 2.9382,
    "solvedtags": [
      {
        "bojTagId": 80,
        "key": "two_pointer"
      }
    ],
    "lastupdate": 1687116861.597403
  },
  "2230": {
    "problemId": "2230",
    "problemLevel": 11,
    "problemName": "수 고르기",
    "average_try": 3.2988,
    "solvedtags": [
      {
        "bojTagId": 97,
        "key": "sorting"
      },
      {
        "bojTagId": 80,
        "key": "two_pointer"
      }
    ],
    "lastupdate": 1687116861.597421
  },
  "14921": {
    "problemId": "14921",
    "problemLevel": 11,
    "problemName": "용액 합성하기",
    "average_try": 2.2577,
    "solvedtags": [
      {
        "bojTagId": 97,
        "key": "sorting"
      },
      {
        "bojTagId": 80,
        "key": "two_pointer"
      }
    ],
    "lastupdate": 1687116861.597439
  },
  "9024": {
    "problemId": "9024",
    "problemLevel": 11,
    "problemName": "두 수의 합",
    "average_try": 2.4046,
    "solvedtags": [
      {
        "bojTagId": 12,
        "key": "binary_search"
      },
      {
        "bojTagId": 97,
        "key": "sorting"
      },
      {
        "bojTagId": 80,
        "key": "two_pointer"
      }
    ],
    "lastupdate": 1687116861.597457
  },
  "1484": {
    "problemId": "1484",
    "problemLevel": 11,
    "problemName": "다이어트",
    "average_try": 2.7561,
    "solvedtags": [
      {
        "bojTagId": 124,
        "key": "math"
      },
      {
        "bojTagId": 80,
        "key": "two_pointer"
      }
    ],
    "lastupdate": 1687116861.597474
  },
  "13422": {
    "problemId": "13422",
    "problemLevel": 12,
    "problemName": "도둑",
    "average_try": 3.4,
    "solvedtags": [
      {
        "bojTagId": 68,
        "key": "sliding_window"
      },
      {
        "bojTagId": 80,
        "key": "two_pointer"
      }
    ],
    "lastupdate": 1687116861.597491
  },
  "15831": {
    "problemId": "15831",
    "problemLevel": 13,
    "problemName": "준표의 조약돌",
    "average_try": 2.9032,
    "solvedtags": [
      {
        "bojTagId": 80,
        "key": "two_pointer"
      }
    ],
    "lastupdate": 1687116861.597509
  },
  "20366": {
    "problemId": "20366",
    "problemLevel": 13,
    "problemName": "같이 눈사람 만들래?",
    "average_try": 3.2521,
    "solvedtags": [
      {
        "bojTagId": 97,
        "key": "sorting"
      },
      {
        "bojTagId": 80,
        "key": "two_pointer"
      }
    ],
    "lastupdate": 1687116861.597526
  },
  "6137": {
    "problemId": "6137",
    "problemLevel": 12,
    "problemName": "문자열 생성",
    "average_try": 4.1511,
    "solvedtags": [
      {
        "bojTagId": 33,
        "key": "greedy"
      },
      {
        "bojTagId": 158,
        "key": "string"
      },
      {
        "bojTagId": 80,
        "key": "two_pointer"
      }
    ],
    "lastupdate": 1687116861.597543
  },
  "3151": {
    "problemId": "3151",
    "problemLevel": 12,
    "problemName": "합이 0",
    "average_try": 4.5178,
    "solvedtags": [
      {
        "bojTagId": 12,
        "key": "binary_search"
      },
      {
        "bojTagId": 125,
        "key": "bruteforcing"
      },
      {
        "bojTagId": 97,
        "key": "sorting"
      },
      {
        "bojTagId": 80,
        "key": "two_pointer"
      }
    ],
    "lastupdate": 1687116861.59756
  },
  "20442": {
    "problemId": "20442",
    "problemLevel": 14,
    "problemName": "ㅋㅋ루ㅋㅋ",
    "average_try": 2.8935,
    "solvedtags": [
      {
        "bojTagId": 80,
        "key": "two_pointer"
      }
    ],
    "lastupdate": 1687116861.597577
  },
  "21279": {
    "problemId": "21279",
    "problemLevel": 16,
    "problemName": "광부 호석",
    "average_try": 4.0847,
    "solvedtags": [
      {
        "bojTagId": 175,
        "key": "data_structures"
      },
      {
        "bojTagId": 59,
        "key": "priority_queue"
      },
      {
        "bojTagId": 65,
        "key": "segtree"
      },
      {
        "bojTagId": 80,
        "key": "two_pointer"
      }
    ],
    "lastupdate": 1687116861.597594
  },
  "2428": {
    "problemId": "2428",
    "problemLevel": 8,
    "problemName": "표절",
    "average_try": 3.2694,
    "solvedtags": [
      {
        "bojTagId": 12,
        "key": "binary_search"
      },
      {
        "bojTagId": 97,
        "key": "sorting"
      }
    ],
    "lastupdate": 1687116861.597612
  },
  "21921": {
    "problemId": "21921",
    "problemLevel": 8,
    "problemName": "블로그",
    "average_try": 2.4961,
    "solvedtags": [
      {
        "bojTagId": 139,
        "key": "prefix_sum"
      },
      {
        "bojTagId": 68,
        "key": "sliding_window"
      }
    ],
    "lastupdate": 1687116861.59763
  },
  "22862": {
    "problemId": "22862",
    "problemLevel": 11,
    "problemName": "가장 긴 짝수 연속한 부분 수열 (large)",
    "average_try": 2.4435,
    "solvedtags": [
      {
        "bojTagId": 80,
        "key": "two_pointer"
      }
    ],
    "lastupdate": 1687116861.597647
  },
  "22945": {
    "problemId": "22945",
    "problemLevel": 12,
    "problemName": "팀 빌딩",
    "average_try": 2.1238,
    "solvedtags": [
      {
        "bojTagId": 80,
        "key": "two_pointer"
      }
    ],
    "lastupdate": 1687116861.597665
  }
}


def transform_data(data: Dict) -> List[Dict]:
    prob_items = []

    for problem in data.values():
        prob_item = {
            "level": problem["problemLevel"],
            "problemId": int(problem["problemId"]),
            "tags": [
                {
                    "bojTagId": tag["bojTagId"],
                    "key": tag["key"]
                } for tag in problem["solvedtags"]
            ],
            "titleKo": problem["problemName"]
        }

        prob_items.append(prob_item)

    return prob_items

transformed_data = transform_data(data)
print(json.dumps(transformed_data, ensure_ascii=False, indent=2))