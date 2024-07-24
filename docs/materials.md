# Environment Setting

For this project, we set up the Minecraft client and server deviant from the official version. Here, we use HMCL client for its user-friendly UX and powerful features, and paper server for its GUI server management and more.

## Launch the client and server

In `ext/mc-client/mc-client-hmcl-1.19.4` find the `HMCL-3.5.8.249.jar` and `paper-1.19.4-550.jar` in the `ext/mc-server/mc-server-paper-1.19.4`. These two `.jar` are the executable files for the client and server.

Run `launch-server.sh` in the root to automatically start the server and `launch-client.sh` to start the client, and in the client choose:
1. multiple user for the client-server mode;
2. select "local server" to connect to the server.

