import requests

NESW = [(-1, 0), (0, 1), (1, 0), (0, -1)]
CORNERS = [(-1, 1), (1, 1), (-1, -1), (1, -1)]
ALL = NESW + CORNERS

#from github.com/evanphoward
def str_input(year, day):
    if year == 0 and day == 0:
        print("SET YEAR AND DAY VALUES!")
        exit(1)
    try:
        return open(f"_{year}/Day{day}/Input.txt").read()
    except FileNotFoundError:
        target_url = 'https://www.adventofcode.com/20' + str(year) + '/day/' + str(day) + '/input'
        session_key = open("Shortcuts/session-key").read().strip()
        response = requests.get(target_url, cookies={'session':session_key}).text.rstrip()
        if response.startswith("Please don't repeatedly"):
            return ''
        open(f"_{year}/Day{day}/Input.txt", "w").write(response)
        return response
    
def graph_input(year, day):
    graph = {}
    inp = str_input(year, day)
    for r, row in enumerate(inp.split("\n")):
        for c, cell in enumerate(row):
            try:
                graph[r, c] = int(cell)
            except:   
                graph[r, c] = cell
    return graph

def check_coord(graph, coord, dirs):
    surr = []
    for dir in dirs:
        new = (coord[0] + dir[0], coord[1] + dir[1])
        if new in graph:
            surr.append((new, graph[new]))
    return surr

def dimension(year, day):
    grid = str_input(year, day).split("\n")
    width, height = len(grid[0]), len(grid)
    return (width, height)