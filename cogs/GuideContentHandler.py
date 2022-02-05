import discord
from discord.ext import commands


class GuideContentHandler(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def 가이드(self, ctx, guide=None):
        if guide == None:
            embed = discord.Embed(title="!가이드 명령어 설명",
                                  description="!가이드 명령어에 대하여 설명합니다.")

            embed.add_field(name="!가이드 [육성, 아이템, 각인, 골드]",
                            value="육성의 경우 캐릭터 육성(또는 게임 전반적인 시스템)에 대하여 정보를 호출합니다.\n",
                            inline=False)

            embed.add_field(name="아이템",
                            value="아이템의 경우 아이템 세팅 방법 또는 아이템의 세트옵션 등에 대하여 정보를 호출합니다.\n",
                            inline=False)

            embed.add_field(name="각인",
                            value="각인의 경우 각인 세팅 방법 또는 각인 효과에 대하여 정보를 호출합니다.\n",
                            inline=False)

            embed.add_field(name="골드",
                            value="골드의 경우 골드 수급 방법에 대하여 정보를 호출합니다.")

            embed.set_footer(text="가이드의 경우 정보가 계속해서 추가됩니다.")

            await ctx.send(embed=embed)
        else:
            if guide == "육성":
                await ctx.send("육성 가이드 정보를 호출합니다\n"
                               "아이템 레벨 올리기(~1415까지)\n"
                               "https://arca.live/b/lostark/29674537?mode=best&p=1\n")

                await ctx.send("아이템 레벨 올리기 - 2\n"
                               "https://arca.live/b/lostark/29671166?mode=best&p=1\n")

            elif guide == "아이템":
                await ctx.send("아이템 가이드 정보를 호출합니다\n"
                               "1370 아르고스 아이템 어떤걸 맞춰야 하나요?\n"
                               "https://arca.live/b/lostark/29703275?mode=best&p=1")

            elif guide == "골드":
                await ctx.send("골드 수급처 - 1\n"
                               "https://arca.live/b/lostark/29692132?mode=best&p=1\n")

                await ctx.send("골드 수급처 - 2\n"
                               "https://arca.live/b/lostark/29700252?mode=best&p=1\n")

            elif guide == "각인":
                await ctx.send("각인 맞추기\n"
                               "https://arca.live/b/lostark/29683873?mode=best&p=1\n")

            else:
                await ctx.send(guide + " 부분의 가이드는 아직 제공되지 않았거나 존재하지 않는 부분입니다.")

    @commands.command()
    async def 각인(self, ctx, *engrave_name):
        input_data = ' '.join(engrave_name)

        engrave_diclist = {
            '각성': '각성기의 재사용 대기시간이 10%/25%/50% 감소하고 사용 가능 횟수가 1회/2회/3회 증가한다.',

            '결투의 대가': '헤드어택 성공 시 피해량이 추가로 5%/12%/25% 증가한다.',

            '굳은 의지': '피격 이상 중 받는 피해가 5%/15%/30% 감소한다.',

            '구슬동자': '적을 타격 시 일정 확률로 자신의 8m 이내에 에테르를 생성한다. 재사용 대기시간 60초/30초/10초',

            '급소 타격': '무력화 공격 시 주는 무력화 수치가 6%/18%/26% 증가한다.',

            '기습의 대가': '백어택 성공 시 피해량이 추가로 5%/12%/25% 증가한다.',

            '달인의 저력': '생명력이 50% 이하일 때, 적에게 주는 피해량이 3%/8%/16% 증가한다.',

            '돌격대장': '기본 이동 속도 증가량 %의 10%/22%/45% 만큼 적에게 주는 피해량이 증가한다.',

            '마나 효율 증가': '마나 회복 속도가 5%/15%/30% 증가하며 마나가 50% 이하일 때 적에게 주는 피해가 3%/6%/12% 증가한다.',

            '바리케이드': '실드 효과가 적용되는 동안 적에게 입히는 피해가 3%/8%/16% 증가한다.',

            '부러진 뼈': '무력화된 대상에게 주는 피해가 7.5%/20%/45% 증가한다.',

            '불굴': '잃은 생명력에 비례하여 받는 피해가 최대 5%/15%/30%까지 감소한다.',

            '선수필승': '생명력이 최대(100%)인 시드 등급 이하 몬스터에게 공격 적중 시 반드시 치명타로 적중하며 해당 치명타는 30%/80%/160% 추가 치명타 피해량을 준다.',

            '슈퍼 차지': '차지 스킬의 차징 속도가 8%/20%/40% 증가하고, 피해량이 4%/10%/20% 증가한다.',

            '안정된 상태': '자신의 생명력이 80% 이상일 때 주는 피해가 3%/8%/16% 증가한다.',

            '약자 무시': '생명력이 30%이하인 적 타격 시 주는 피해가 9%/22%/36% 증가한다.',

            '에테르 포식자': ('적을 타격 시 자신만 획득할 수 있는 에테르를 생성한다. '
                        '에테르 습득 시 90초 동안 공격력이 0.2%/0.3%/0.5% 증가하고 모든 방어력이 0.3%/0.6%/1.0% 증가하며 최대 30중첩까지 습득할 수 있다. '
                        '에테르 습득 시 일정 확률로 3중첩 증가한다. (발동 재사용 대기시간 10초)'),

            '예리한 둔기': '치명타 피해량이 10%/25%/50% 증가하지만, 공격 시 일정 확률로 20% 감소된 피해를 준다.',

            '원한': '보스 등급 이상 몬스터에게 주는 피해가 4%/10%/20% 증가하지만, 받는 피해가 20% 증가한다.',

            '위기 모면': '죽음에 이르는 피해를 입으면 3초간 무적이 되며, 해당 효과 적용 중 받은 피해의 50%를 회복한다. (재사용 시간 15분/12분/9분)',

            '저주받은 인형': '공격력이 3%/8%/16% 증가하지만, 받는 생명력 회복 효과가 25% 감소한다. (자연 회복 제외)',

            '정기 흡수': '공격 및 이동속도가 3%/8%/15% 증가한다.',

            '중갑 착용': '모든 방어력이 2%/50%/100% 증가한다. 중갑 착용으로 인하여 증가한 방어력은 방어력 감소 효과에 영향받지 않는다(방감 각인 포함)',

            '최대 마나 증가': '최대 마나가 5%/15%/30% 증가한다.',

            '폭발물 전문가': '폭탄 및 수류탄 배틀아이템의 소지 가능 개수가 1개/2개/3개 증가한다.',

            '질량 증가': '공격속도가 10% 감소하지만, 공격력이 4%/10%/18% 증가한다.',

            '타격의 대가': '공격 타입이 백 어택 및 헤드 어택에 해당되지 않는 공격의 피해가 3%/8%/16% 증가한다. 각성기는 해당 효과에서 제외된다.',

            '시선 집중': ('일반 채팅에 !!!!! 가 포함된 문구가 출력될 경우 해당 효과가 6초간 발동된다. 1회에 한하여 효과 발동 이후 사용한 공격 스킬의 피해량이'
                      '8%/16%/28% 증가한다. 각성기 피해량은 해당 수치의 절반만 적용된다. (발동 재사용 대기시간 30초)'),

            '아드레날린': ('이동기 및 기본공격을 제외한 스킬사용 후 6초 동안 공격력이 0.3%/0.6%/1% 증가하며(최대 6중첩) '
                      '해당 효과가 최대 중첩 도달 시 치명타 적중률이 추가로 5%/10%/15% 증가한다. '
                      '해당 효과는 스킬 취소에 따른 재사용 대기시간 감소가 적용되는 경우, 스킬 종료 후 적용된다.'),

            '속전속결': '홀딩 및 캐스팅 스킬의 홀딩, 캐스팅 속도가 5%/10%/20% 증가하고, 피해량이 4%/10%/20% 증가한다',

            '전문의': ('자신 및 파티원에게 사용하는 쉴드 및 생명력 회복 효과가 6%/14%/24% 증가하고 '
                    '대상의 생명력이 50% 이하인 경우 해당 효과가 추가로 3%/7%/12% 증가한다.'),

            '정밀 단도': '치명타 적중률이 4%/10%/20% 증가하지만 치명타 피해가 12% 감소한다.',

            '공격력 감소': '공격력이 2%/4%/6% 감소한다',

            '공격속도 감소': '공격속도가 2%/4%/6% 감소한다.',

            '방어력 감소': '방어력이 5%/10%/15% 감소하며 중갑 착용 각인 효과로 감소 효과를 지울 수 있다',

            '이동속도 감소': '이동속도가 2%/4%/6% 감소한다.',

            # ================================= 여기서부턴 직업 각인 영역입니다. ===========================================

            '갈증': '(리퍼 전용) 혼돈 게이지 획득량이 30% 증가하며, 혼돈 게이지가 가득 찰 때 공격력이 12%/18%/25% 증가하는 효과를 추가로 획득한다.',

            '강화 무기': '(데빌헌터 전용) 스탠스 변경 시 9초동안 치명타 적중률이 20%/25%30% 증가한다.',

            '고독한 기사': ('(워로드 전용) 랜스 스킬의 치명타 적중률이 5%/10%/15% 및 치명타 피해가 30%/40%/50% 증가하지만, '
                       '전장의 방패를 사용할 수 없으며 방어태세 중 실드 게이지의 소모량이 100% 증가한다.'),

            '광기': ('(버서커 전용) 분노 게이지가 항상 최대치로 유지되며, 폭주 시 어둠의 힘을 이용한 폭주 상태가 된다. '
                   '폭주 상태에서 적에게 주는 피해가 4%/9%/18% 증가하고, 공격 및 이동속도가 15.0% 증가하며 받는 모든 피해가 65.0% 감소한다. '
                   '하지만, 폭주 상태가 되는 순간 최대 생명력의 25.0%로 전환되며, 생명력 회복 효과가 적용되더라도 이를 초과할 수 없게 된다. 실드 효과가 25%만 적용된다. '
                   ' X키를 통해 폭주를 해제할 수 있으며 해제 즉시 최대 생명력의 25.0%를 회복하지만, 30초 동안 폭주를 할 수 없게 된다.'),

            '광전사의 비기': '(버서커 전용) 폭주 중 치명타 피해가 30%/40%/50% 증가하고 폭주 종료 시 탈진 효과가 발생하지 않는다.',

            '극의: 체술': '(인파이터 전용) 기력 에너지의 자연 회복 속도가 300%/450%/600% 증가하며 기력 스킬의 피해량이 30%/45%/60% 증가하지만 충격 스킬의 피해량이 30% 감소한다.',

            '넘치는 교감': '(서머너 전용) 마리린, 파우루, 엘씨드, 슈르디, 켈시온의 소환 유지 시간이 20%/25%/30% 증가하고 피해량이 10%/15%/20% 증가한다.',

            '달의 소리': '(리퍼 전용) 페르소나 상태로 전환 시 매초 중첩되는 급습 강화 효과 대신 급습 피해가 120%/140%/160% 증가하는 효과를 획득한다.',

            '두 번쨰 동료': ('(호크아이 전용) 실버호크 MK-II 를 소환하여 파티원의 이동속도가 추가로 4% 증가하며, '
                        '실버호크의 기본 공격 범위가 60%, 기본 공격 피해량이 100%/200%/300% 및 소환 유지시간이 30%/60%/100% 증가한다. '
                        '또한 실버호크 기본 공격 및 폭풍의 날개 적중 시 대상에게 죽음의 표적을 추가하여 나에게 받는 피해가 4%/9%/14% 증가한다. '
                        '추가로 전투 중 호크게이지의 자연 회복량이 10%/20%/30% 증가한다.'),

            '멈출 수 없는 충동': ('(데모닉 전용) 악마화 종료 시 평정심 효과가 발생하지 않는다. '
                           '악마화 시 악마화 스킬의 재사용 대기시간이 초기화 되며 악마화 중 치명타 적중률이 0%/15%/30% 증가한다.'),

            '버스트': ('(블레이드 전용) 블레이드 버스트 스킬 사용 시 보유한 블레이드 오브 개수와 상관없이 최고 단계의 블레이드 버스트가 발동된다. '
                    '또한 아츠 발동 중 평타 및 각성기를 제외한 스킬 적중 시 0.4초 마다 버스트 강화효과가 중첩된다. (최대 20중첩)'
                    ' 해당 효과는 블레이드 버스트 스킬의 피해량을 7.5% 증가 및 공격력을 0%/0.5%/1.0% 증가 시킨다. '
                    '추가로 블레이드 아츠 종료 시 보유한 버스트 강화 효과의 개수만큼 블레이드 오브 게이지를 획득한다. (개당 5%)'),

            '분노의 망치': '(디스트로이어 전용) 해방 스킬 사용 시 소모한 코어 수에 비례하여 치명타 적중률이 3%/4%/5%, 치명타 피해량이 5%/10%/15% 증가한다.',

            '사냥의 시간': '(건슬링어 전용) 핸드건 및 라이플 스킬의 치명타 적중률이 20%/27%/35% 증가하지만 샷건 스탠스를 사용할 수 없다.',

            '상급 소환사': '(서머너 전용) 고대의 정령 스킬의 구슬 소모 개수가 1개 감소하고 모든 속성 피해량이 5%/10%/15% 증가한다.',

            '세맥타통': ('(기공사 전용) 내공 수치가 1미만으로 떨어지지 않으나 금강선공 중 추가 내공 회복 효과가 적용되지 않는다.'
                     '내공 수치가 30% 미만일 시 적에게 주는 피해가 5%/10%/15% 증가한다.'),

            '심판자': '(홀리나이트 전용) 징벌 스킬의 피해량이 15%/20%/25%, 징벌 스킬 타격 시 신앙게이지 획득량이 100% 증가한다. 신의 집행자 지속 시간이 100% 증가한다.',

            '아르데타인의 기술': ('(스카우터 전용) 드론 및 합작 스킬의 피해량이 15%/20%/25% 증가하며, 배터리의 최대량이 10%/15%/20% 증가한다. '
                          '또한 드론이 스카우터에게 부착할 시 이동속도가 10% 증가한다.'),

            '역천지체': '(기공사 전용) 금강선공 시 즉시 3단계로 진입하며, 금강선공 상태일 때 내공 회복 속도가 200% 증가하고 피해량 증가 효과가 추가로 10%/20%/30% 증가한다.',

            '포격 강화': ('(블래스터 전용) 포격 스킬의 피해량이 20%/30%/40% 증가하며 화력 버프가 없을 시 화력 게이지의 획득량이 10%/20%/30% 증가한다.'
                      '또한 화력 게이지가 모두 충전되면 쿨링 효과를 제거한다.'),

            '오의 강화': '(배틀마스터 전용) 엘리멘탈 구슬의 최대 개수가 1개 증가하며, 오의 스킬 사용 시 보유한 엘리멘탈 구슬 1개 당 적에게 주는 피해가 8%/10%/12% 증가한다.',

            '완벽한 억제': '(데모닉 전용) 일반 스킬의 피해량이 20%/25%/30% 증가하며, 모든 스킬의 잠식 게이지 획득량이 50% 증가하지만, 악마화 변신은 불가능하다.',

            '잔재된 기운': ('(블레이드 전용) 아츠 발동 시 2초 동안 아츠 게이지가 감소되지 않으며 버스트 사용 시 버스트 단계에 따라 30초 동안 공격/이동속도가 6%/9%/12%'
                       '및 공격력이 (8%, 16%, 25%)/(10%, 20%, 30%)/(12%, 24%, 36%) 증가한다.'),

            '전투 태세': ('(워로드 전용) 일반 스킬의 피해량이 20% 증가하고 방어 태새의 실드량이 30%/40%/50% 증가한다.'
                      '방어 태세 중 피격 시 10초 동안 적에게 주는 피해량이 4%/5%/6% 증가하는 효과를 획득하며 해당 효과는 3회까지 중첩 가능하고 1초에 1회만 획득 가능하다.'),

            '절실한 구원': '(바드 전용) 회복 효과가 종료될 때 추가로 회복 효과가 발동되어 자신 및 파티원에게 자신의 최대 생명력의 8%/16%/24% 만큼 추가 회복한다.',

            '절정': '(창술사 전용) 듀얼 게이지 3단계가 가득 찬 상태에서 스탠스 전환 시 획득하는 난무/집중 3단계 효과 대신 강화된 (난무/집중1)/(난무/집중2)/(난무/집중3)을 획득한다.',

            '절제': '(창술사 전용) 집중 스탠스를 사용할 수 없지만 난무 스킬의 피해량이 18%/27%/36% 증가한다.',

            '죽음의 습격': '(호크아이 전용) 최후의 습격 스킬 사용 시 남은 호크 게이지의 50%를 돌려받으며, 적중된 대상이 자신에게 받는 피해가 8초동안 20%/30%.40% 증가한다.',

            '중력 수련': ('(디스트로이어 전용) 전투 중 중력 게이지가 초당 1.0%/1.5%/2.0%씩 자연 회복된다.'
                      '또한 중력 가중 모드 시 평타와 볼텍스 그라비티의 치명타 적중률이 10% 증가하며 적에게 주는 피해가 4%/10%/20% 증가한다.'),

            '진실된 용맹': '(바드 전용) 용맹의 세레나데 사용 시 자신이 적에게 주는 피해량이 추가로 10%/15%/20% 증가하고, 치명타 적중률이 10% 증가한다.',

            '진화의 유산': ('(스카우터 전용) 하이퍼 싱크 모드 중 싱크 스킬이 적중했을 시 피해량이 2%/4%/6% 증가하는 효과를 획득하며 (최대 3중첩)'
                       ' 다른 싱크 스킬들의 재사용 대기시간이 0.5초씩 감소한다. 또한 하이퍼 싱크 모드가 해제될 시 소모한 코어 에너지의 40%를 돌려받는다.'),

            '초심': '(배틀마스터 전용) 적에게 주는 피해가 15%/20%/25% 증가하지만, 더 이상 엘리멘탈 게이지를 획득할 수 없다.',

            '축복의 오라': ('(홀리나이트 전용) 신성의 오라 사용 시 추가로 받는 피해가 10%/15%/20% 감소되고,'
                       '회복 효과가 발동되어 자신 및 파티원이 매 2.5초/2.0초/1.5초 마다 자신의 생명력의 2% 만큼 회복한다.'),

            '충격 단련': '(인파이터 전용) 충격 스킬의 피해량이 10%/15%/20% 증가하며, 매 초 마다 최대 충격 에너지의 2%/3%/4%를 회복한다.',

            '피스메이커': ('(건슬링어 전용) 핸드건 스탠스로 변경 시 공격속도 8%/12%/16% 증가, '
                      '샷건 스탠스로 변경 시 치명타 적중률 15%/20%/25% 증가, '
                      '라이플 스탠스로 변경 시 적에게 주는 피해가 10% 증가 및 생명력이 50% 이하인 대상에게 주는 피해가 추가로 10%/20%/30% 증가하는 효과를 9초동안 획득한다.'),

            '헨드거너': ('(데빌헌터 전용) 헨드건 스탠스만 사용할 수 있지만, 핸드건 스킬의 피해량이 30% 증가 및 무력화 피해가 40% 증가한다.'
                     ' 또한 각성기의 피해량이 15%/22%/30% 증가한다.'),

            '화력 강화': ('(블래스터 전용) 받는 피해가 20% 감소한다. '
                      '또한 화력 버프의 단계에 따라 치명타 적중률이 (15%, 22%, 30%)/(20%, 27%, 35%)/(25%, 32%, 40%) 증가한다.'),

            '황제의 칙령': ('(아르카나 전용) 일반 스킬의 덱 게이지 획득량이 50% 증가하고 피해량이 10%/20%/30% 증가하며, 카드덱에 황제 카드가 추가된다. '
                       '황제 카드는 사용 시 주변에 큰 피해를 준다.'),

            '황후의 은총': '(아르카나 전용) 4스택 루인 피해량이 20%/25%/30% 증가하고 루인 스킬 적중 시 소모된 마나의 30%를 회복한다.',

            '일격필살': ('(스트라이커 전용) 엘리멘탈 구슬의 최대 개수가 1개 증가하며, 오의 스킬 사용 시 남아있는 엘리멘탈 구슬을 추가로 모두 소모한다. '
                     '추가로 소모한 엘리멘탈 구슬 당 해당 오의 스킬의 피해량이 17%/26%/35% 증가한다.'),

            '오의난무': '(스트라이커 전용) 오의 스킬 사용 시 엘리멘탈 구슬을 반드시 1개만 소모하며, 오의 스킬의 피해가 8% 증가한다.',

            '점화': ('(소서리스 전용) 마력 해방 발동 시 각성기 및 이동기를 제외한스킬의 남은 재사용 대기시간이 50%로 감소하며,'
                   ' 마력 해방 중 치명타 적중률이 10%/17%/25%, 치명타 피해가 20%/35%/50% 증가한다.'),

            '환류': '(소서리스 전용) 마력 방출을 사용 할 수 없지만, 각성기 및 이동기를 제외한 스킬의 피해량이 8%/12%/16% 만큼 증가하고 재사용 대기시간이 3%/7%/10% 감소한다.',

            '회귀': '(도화가 전용) 저무는 달 및 떠오르는 해 스킬 사용 시, 자신에게 60초 동안 치명타 적중률 6%/9%/12% 및 치명타 피해가 20%/30%/40% 증가하는 효과를 부여한다.',

            '만개': ('(도화가 전용) 해 구슬 획득 시 떠오르는 해의 기운이 널리 퍼져 구슬을 획득한 대상을 포함한 24m 범위 내에 있는 파티원에게 '
                   '도화가의 최대 생명력 7%/11%/15%에 해당하는 생명력을 회복시킨다')
        }

        engrave_nickname_list = [
            ['결투의 대가', '결대'],
            ['구슬동자', '구동'],
            ['급소 타격', '급타'],
            ['기습의 대가', '기습', '기대'],
            ['달인의 저력', '달저'],
            ['돌격대장', '돌대'],
            ['마나 효율 증가', '마효증'],
            ['바리케이드', '바리'],
            ['부러진 뼈', '부뼈'],
            ['선수필승', '선필'],
            ['슈퍼 차지', '슈차'],
            ['안정된 상태', '안상'],
            ['약자 무시', '약무'],
            ['에테르 포식자', '에포', '에테르', '포식자'],
            ['예리한 둔기', '예둔'],
            ['저주받은 인형', '저받', '저받인'],
            ['정기 흡수', '정흡'],
            ['중갑 착용', '중갑'],
            ['최대 마나 증가', '최마증'],
            ['폭발물 전문가', '폭전'],
            ['질량 증가', '질증'],
            ['타격의 대가', '타대'],
            ['시선 집중', '시집'],
            ['아드레날린', '아드'],
            ['속전속결', '속속'],
            ['정밀 단도', '정단', '정밀단또'],
            ['공격력 감소', '공감'],
            ['방어력 감소', '방감'],
            ['공격속도 감소', '공속감'],
            ['이동속도 감소', '이속감'],
            ['강화 무기', '강무'],
            ['고독한 기사', '고기'],
            ['광기', '팡기'],
            ['광전사의 비기', '비기', '광비'],
            ['극의: 체술', '체술'],
            ['넘치는 교감', '교감'],
            ['달의 소리', '달소'],
            ['두 번째 동료', '두동'],
            ['멈출 수 없는 충동', '충동'],
            ['분노의 망치', '분망'],
            ['사냥의 시간', '사시'],
            ['상급 소환사', '상소'],
            ['세맥타통', '세맥', '새맥'],
            ['아르데타인의 기술', '기술'],
            ['역천지체', '역천'],
            ['포격 강화', '포강', '포격'],
            ['오의 강화', '오의'],
            ['완벽한 억제', '억제'],
            ['잔재된 기운', '잔재'],
            ['전투 태세', '전태'],
            ['절실한 구원', '절구'],
            ['죽음의 습격', '죽습'],
            ['중력 수련', '중수'],
            ['진실된 용맹', '진용'],
            ['진화의 유산', '유산'],
            ['축복의 오라', '축오'],
            ['충격 단련', '충단'],
            ['피스메이커', '피메'],
            ['핸드거너', '잼드거너'],
            ['화력 강화', '화강', '화력'],
            ['황제의 칙령', '황제', '칙령'],
            ['황후의 은총', '황후', '은총'],
            ['일격필살', '일필'],
            ['오의난무', '오의스커']
        ]

        for engrave_nickname in engrave_nickname_list:
            if input_data in engrave_nickname:
                input_data = engrave_nickname[0]

        if not input_data:
            embed = discord.Embed(title="!각인 명령어 설명",
                                  description="!각인 명령어에 대하여 설명합니다.")
            embed.add_field(name="!캐릭터정보 [정밀 단도]",
                            value="각 각인의 설명을 호출합니다.\n")
            await ctx.send(embed=embed)
        else:
            if input_data in engrave_diclist:
                embed = discord.Embed(title=input_data + " 각인 설명",
                                      description=engrave_diclist[input_data])

                await ctx.send(embed=embed)
            else:
                await ctx.send(input_data + " 각인은 존재하지 않는 각인이거나 추가되지 않은 각인입니다.")


def setup(bot):
    bot.add_cog(GuideContentHandler(bot))
