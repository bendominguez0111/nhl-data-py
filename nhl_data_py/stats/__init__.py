BASE_URL = "https://statsapi.web.nhl.com/api"
VERSION = "v1"

from nhl_data_py.utils import build_endpoint

# _configurations.py
CONFIGURATIONS_URL = build_endpoint('conferences')

# _expands.py
EXPANDS_URL = build_endpoint('expands')

# _languages.py
LANGUAGES_URL = build_endpoint('languages')

# _platforms.py
PLATFORMS_URL = build_endpoint('platforms')

# _franchises.py
FRANCHISES_URL = build_endpoint('franchises')

# _teams.py
TEAMS_URL = build_endpoint('teams')

# _divisions.py
DIVISIONS_URL = build_endpoint('divisions')

# _conferences.py
CONFERENCES_URL = build_endpoint('conferences')

# _people.py
PEOPLE_URL = build_endpoint('people')
POSITIONS_URL = build_endpoint('positions')

# _game.py
BASE_GAME_URL = build_endpoint('game/{id}')
GAME_LIVE_FEED_URL = build_endpoint('feed/live', base=[BASE_GAME_URL])
GAME_BOXSCORE_URL = build_endpoint('boxscore', base=[BASE_GAME_URL])
GAME_LINESCORE_URL = build_endpoint('linescore', base=[BASE_GAME_URL])
GAME_CONTENT_URL = build_endpoint('content', base=[BASE_GAME_URL])
GAME_TYPES = build_endpoint('gameTypes')
GAME_STATUS = build_endpoint('gameStatus')
GAME_PLAY_TYPES = build_endpoint('playTypes')

# _tournaments.py
TOURNAMENT_TYPES_URL = build_endpoint('tournamentTypes')
PLAYOFF_TOURNAMENTS_URL = build_endpoint('tournaments/playoffs')

# _schedule.py
SCHEDULE_URL = build_endpoint('schedule')

# _seasons.py
SEASONS_URL = build_endpoint('seasons')

# _standings.py
STANDINGS = build_endpoint('standings')
STANDINGS_TYPES_URL = build_endpoint('standingsTypes')

# _stat_types.py
STAT_TYPES_URL = build_endpoint('statTypes')

# _team_stats.py
TEAM_STATS_URL = build_endpoint('teams/{id}/stats')

# _draft.py
CY_DRAFT_URL = build_endpoint('draft')
PY_DRAFT_URL = build_endpoint('draft/{year}')

# _prospects.py
PROSPECTS_URL = build_endpoint('prospects')

# _awards.py
AWARDS_URL = build_endpoint('awards')

# _venues.py
VENUES_URL = build_endpoint('venues')

# _event_types.py
EVENT_TYPES_URL = build_endpoint('eventTypes')

# performer_types.py
PERFORMER_TYPES_URL = build_endpoint('performerTypes')

from nhl_data_py.stats._configurations import *
from nhl_data_py.stats._expands import *
from nhl_data_py.stats._languages import *
from nhl_data_py.stats._platforms import *
from nhl_data_py.stats._franchises import *
from nhl_data_py.stats._teams import *
from nhl_data_py.stats._divisions import *
from nhl_data_py.stats._conferences import *
from nhl_data_py.stats._people import *
from nhl_data_py.stats._game import *
from nhl_data_py.stats._tournaments import *
from nhl_data_py.stats._schedule import *
from nhl_data_py.stats._seasons import *
from nhl_data_py.stats._standings import *
from nhl_data_py.stats._stat_types import *
from nhl_data_py.stats._team_stats import *
from nhl_data_py.stats._draft import *
from nhl_data_py.stats._prospects import *
from nhl_data_py.stats._awards import *
from nhl_data_py.stats._venues import *
from nhl_data_py.stats._event_types import *
from nhl_data_py.stats._performer_types import *
