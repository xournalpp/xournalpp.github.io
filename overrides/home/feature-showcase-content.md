{% set feature_list = 
    [
        ({
        "title": "Handwrite your notes",
        "description_list":
            [
                "Support for pressure-sensitive stylus and drawing tablets (Wacom, Huion, XP-Pen, etc.)",
                "Robust and customizable pen, highlighter and eraser tools, allowing you to write how you want to write"
            ], 
        "documentation_link": "#",
        "demonstration_video_link": "#", 
        "image_filename": "Handwritten.png"
        }),

        ({
        "title": "Keep your work organized",
        "description_list":
            [
                "Use layers to make complex notes that are still pleasant to work with",
                "Keep track of the notes by using page previews"
            ], 
        "documentation_link": "#",
        "demonstration_video_link": "#", 
        "image_filename": "Layers.gif"
        }),

        ({
        "title": "Enhance and accelerate your note-taking",
        "description_list":
            [
                "Add images and create various shapes, from circles to splines to axis",
                "Snap objects to rectangular grid or degrees of rotation"
            ], 
        "documentation_link": "#",
        "demonstration_video_link": "#",
        "image_filename": "Create Shape.png"
        }),

        ({
        "title": "Get scientific",
        "description_list":
            [
                "Create anything from differential equations to electrical circuits or the structural formula of molecules using our built-in LaTeX editor"
            ],
        "documentation_link": "#",
        "demonstration_video_link": "#",
        "image_filename": "Latex.png"
        }),
        
        ({
        "title": "Your notes, your way",
        "description_list":
            [
                "Customize your toolbar to create a new layout, tailor-made for you",
                "Use a plugin or create your own via the Lua programming language"

            ],
        "documentation_link": "#",
        "demonstration_video_link": "#",
        "image_filename": "Customize Toolbars.png"
        }),

        ({
        "title": "Explain every stroke",
        "description_list":
            [
                "Record audio while you write and insert the recording to any object in your note",
                "Listen to the recorded audio with the 'play object' tool"

            ],
        "documentation_link": "#",
        "demonstration_video_link": "#", 
        "image_filename": "Audio Note.png"
        }),
    ] 
%}

{% macro feature_showcase(feature_showcase_properties, chirality) -%}
    <div class="feature feature-{{chirality}}">
        <div class="feature-text">
            <h2>{{ feature_showcase_properties["title"] }}</h2>
            <div class="feature-description-container">
            {% for description in feature_showcase_properties["description_list"] %}
                <div class="feature-description">
                    <p class="bullet-point">|</p><p>{{description}}</p>
                </div>
            {% endfor %}
            </div>
            <div class="feature-link">
                <a href= {{ feature_showcase_properties['documentation_link'] }} class="documentation-link">Learn more</a>
                <a href= {{ feature_showcase_properties['demonstration_video_link'] }} class="video-link">Watch demonstration video</a>
            </div>
        </div>
        <img src= "/img/{{ feature_showcase_properties['image_filename'] }}">
	</div>
{%- endmacro %}

{% for feature_showcase_properties in feature_list %}
    {% if loop.index%2 == 0 %}
        {{ feature_showcase(feature_showcase_properties, "left") }}
    {% else %}
        {{ feature_showcase(feature_showcase_properties, "right") }}
    {% endif %}
{% endfor %}

