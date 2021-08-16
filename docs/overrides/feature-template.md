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

<!-- title, chirality, description_list, image_filename, documentation_link, demonstration_video_link -->