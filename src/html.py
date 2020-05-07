def HtmlGenerator(output):
    html = """<html>

    <head>
        <meta charset="UTF-8">
        <title>Smaps - Results</title>
        <meta name="viewport" content="width=device-width, initial-scale=1">


        <style>
            @font-face {
                font-family: facebook;
                src: url(https://s3-us-west-2.amazonaws.com/s.cdpn.io/23596/facebook-letter-faces.ttf);
            }

            @import url("http://fonts.googleapis.com/css?family=Lato:300,400,700|Donegal+One|Source+Code+Pro:400");

            #container {
                max-width: 80%;
                padding: 10px 20px;
                background: #eaebed;
                margin: 10px auto;
                padding: 20px;
                background: #eaebed;
                border-radius: 8px;
                font-family: 'Lato';
            }

            .title {
                text-transform: uppercase;
                text-align: center;
                margin-bottom: 30px;
                color: #345689;
                font-weight: 300;
                font-size: 24px;
                letter-spacing: 1px;
                width: 100%;
                font-family: 'Lato'
            }

            .buttonDefault {
                display: inline-block;
                position: relative;
                padding: 10px 25px;

                background-color: #345689;
                color: white;

                font-family: 'Lato';
                text-decoration: none;
                font-size: 0.9em;
                text-align: center;
            }

            .buttonDefault:hover {
                background-color: #333;
                color: white;
                cursor: pointer;
            }

            .buttonDownload {
                display: inline-block;
                position: relative;
                padding: 10px 25px;

                background-color: #345689;
                color: white;

                font-family: 'Lato';
                text-decoration: none;
                font-size: 0.9em;
                text-align: center;
                text-indent: 15px;
            }

            .buttonDownload:hover {
                background-color: #333;
                color: white;
            }

            .buttonDownload:before,
            .buttonDownload:after {
                content: ' ';
                display: block;
                position: absolute;
                left: 15px;
                top: 52%;
            }

            .buttonDownload:before {
                width: 10px;
                height: 2px;
                border-style: solid;
                border-width: 0 2px 2px;
            }

            .buttonDownload:after {
                width: 0;
                height: 0;
                margin-left: 3px;
                margin-top: -7px;

                border-style: solid;
                border-width: 4px 4px 0 4px;
                border-color: transparent;
                border-top-color: inherit;

                animation: downloadArrow 2s linear infinite;
                animation-play-state: paused;
            }

            .buttonDownload:hover:before {
                border-color: white;
            }

            .buttonDownload:hover:after {
                border-top-color: white;
                animation-play-state: running;
            }

            @keyframes downloadArrow {
                0% {
                    margin-top: -7px;
                    opacity: 1;
                }

                0.001% {
                    margin-top: -15px;
                    opacity: 0;
                }

                50% {
                    opacity: 1;
                }

                100% {
                    margin-top: 0;
                    opacity: 0;
                }
            }

            .button {
                text-align: center;
            }

            .accordion label {
                display: block;
                background-color: #eaebed;
                padding: 10px;
                color: #345689;
                text-shadow: 0 0 2px rgba(255, 255, 255, 0.6);
                cursor: pointer;
                border-bottom: 1px solid #bdbdbd;
                border-top: 1px solid #ffffff;
                font-size: 14px;
            }

            .accordion p {
                color: white;
                padding: 10px;
                font-size: 0.9em;
                line-height: 1.7em;
                border-bottom: 1px solid #bdbdbd;
                visibility: hidden;
                opacity: 0;
                display: none;
                text-align: left;
                background-color: #333;
                margin-top: 0px;
                font-family: "Courier New";
            }

            #tm:checked~.hiddentext {
                display: block;
                visibility: visible;
                opacity: 1;
            }

            input#tm {
                display: none;
                position: relative;
            }

            #to:checked~.hiddentext {
                display: block;
                visibility: visible;
                opacity: 1;
            }

            #tn:checked~.hiddentext {
                display: block;
                visibility: visible;
                opacity: 1;
            }

            input#tn {
                display: none;
                position: relative;
            }



            input#to {
                display: none;
                position: relative;
            }

            .w3-modal {
                z-index: 3;
                display: none;
                padding-top: 100px;
                position: fixed;
                left: 0;
                top: 0;
                width: 100%;
                height: 100%;
                overflow: auto;
                background-color: rgb(0, 0, 0);
                background-color: rgba(0, 0, 0, 0.4)
            }

            .w3-modal-content {
                margin: auto;
                background-color: #fff;
                position: relative;
                padding: 0;
                outline: 0;
                width: 95%;
                height: 650px;
            }

            .w3-container,
            .w3-panel {
                padding: 0.01em 16px
            }

            .w3-panel {
                margin-top: 16px;
                margin-bottom: 16px
            }

            .w3-container:after,
            .w3-container:before,
            .w3-panel:after,
            .w3-panel:before,
            .w3-row:after,
            .w3-row:before,
            .w3-row-padding:after,
            .w3-row-padding:before,
            .w3-cell-row:before,
            .w3-cell-row:after,
            .w3-clear:after,
            .w3-clear:before,
            .w3-bar:before,
            .w3-bar:after {
                content: "";
                display: table;
                clear: both;
            }

            .w3-display-topright {
                position: absolute;
                right: 0;
                top: 0
            }

            .w3-btn,
            .w3-button {
                border: none;
                display: inline-block;
                padding: 8px 16px;
                vertical-align: middle;
                overflow: hidden;
                text-decoration: none;
                color: inherit;
                background-color: inherit;
                text-align: center;
                cursor: pointer;
                white-space: nowrap
            }
        </style>
    </head>

    <body>
        <div id="container">
            <br>
            <div class='title'>
                smaps - results
            </div>
            <div class='button'>
                <button onclick="document.getElementById('id01').style.display='block'" class="buttonDefault">Quast</button>
                <br> <br>""" 

    return html
