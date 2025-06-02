# mcp-thisweek

A simple MCP (Model Context Protocol) server that provides the dates for the current week (Monday to Friday) and today's date.

## Features

-   `get_this_week_dates`: Returns a list of dates from Monday to Friday of the current week.
-   `get_today_date`: Returns today's date.

### Examples

-   "What are the dates for this week from Monday to Friday?"
-   "What is today's date?"

## Setup

You can set up and run `mcp-thisweek` using pip and Python, or using Docker.

### Using pip and Python

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/taku-o/mcp-thisweek.git
    cd mcp-thisweek
    ```

2.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Configure your MCP client:**
    Add `mcp-thisweek` to your MCP client's configuration file (e.g., `mcp.json` or `claude_desktop_config.json`).

    Replace `/path/to/` with the actual path to the `mcp-thisweek` directory on your system. You may also need to replace `python` with `/path/to/python` if it's not in your system's PATH.

    ```json
    {
      "mcpServers": {
        "mcp-thisweek": {
          "command": "python",
          "args": [
            "/path/to/mcp-thisweek/server.py"
          ]
        }
      }
    }
    ```

### Using Docker

1.  **Build the Docker image:**
    Navigate to the root directory of the project (where the `Dockerfile` is located) and run:
    ```bash
    docker build -t mcp-thisweek .
    ```

2.  **Run the Docker container:**
    ```bash
    docker run -d --name mcp-thisweek-container mcp-thisweek
    ```
    This will run the container in detached mode.

3.  **Configure your MCP client (for Docker):**
    When using Docker, `fastmcp` needs to communicate with the server running inside the container. `FastMCP` typically uses local command execution. To make this work with Docker, you might need a wrapper script or adjust how `fastmcp` invokes the server if it needs to `docker exec` into the container or if `fastmcp` itself is run inside a Docker network.

    A common way `fastmcp` is used is by specifying a command that `fastmcp` can run. If `fastmcp` is running on the host, it cannot directly execute a Python script inside a Docker container without `docker exec`.

    For a Dockerized `mcp-server`, the `command` in `mcp.json` would typically be `docker exec -i mcp-thisweek-container python /app/server.py`. This assumes `fastmcp` is running on the host and the container is named `mcp-thisweek-container`.

    The JSON configuration for Docker would look like:
    ```json
    {
      "mcpServers": {
        "mcp-thisweek": {
          "command": "docker",
          "args": [
            "exec",
            "-i",
            "mcp-thisweek-container",
            "python",
            "/app/server.py"
          ]
        }
      }
    }
    ```
    Ensure the container `mcp-thisweek-container` is running.

## License

This project is licensed under the MIT License.
