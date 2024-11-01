import minify_html

def define_env(env):
    def mqtt_topic(name, icon):
        segments = name.split("/")
        spans = []
        for i in range(len(segments)):
            segment = segments[i] + "/" if i < len(segments) - 1 else segments[i]
            spans.append(f"""<span style="--idx: {i:d}">{segment:s}</span>""")

        return minify_html.minify(f"""
            <div class="mqtt-topic">
                <div>
                    :material-{icon:s}:
                </div>
                <div>
                    {"".join(spans):s}
                </div>
            </div>
        """)

    @env.macro
    def mqttr(name):
        return mqtt_topic(name, "eye")

    @env.macro
    def mqttw(name):
        return mqtt_topic(name, "pencil")
