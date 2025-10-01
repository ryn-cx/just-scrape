from pathlib import Path

JUST_SCRAPE_DIR = Path(__file__).parent
TEST_FILE_DIR = JUST_SCRAPE_DIR / "_input"
# By default there is a bunch of packages that are excluded, I have no idea why they are
# excluded, but this will match the API request that is sent when visiting the website.
DEFAULT_EXCLUDE_PACKAGES = (
    "3ca",
    "als",
    "amo",
    "cgv",
    "chi",
    "cnv",
    "cut",
    "daf",
    "kod",
    "koc",
    "mrp",
    "mte",
    "mvt",
    "nxp",
    "org",
    "ply",
    "rvl",
    "tak",
    "tbv",
    "tf1",
    "uat",
    "vld",
    "wa4",
    "wdt",
    "yot",
    "yrk",
)
