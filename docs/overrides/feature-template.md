{% macro feature_showcase(title, chirality, description_list, image_filename, documentation_link, demonstration_video_link) -%}
    <div class="feature feature-{{chirality}}">
        <div class="feature-text">
            <h2>{{title}}</h2>
            <div class="feature-description-container">
            {% for description in description_list %}
                <div class="feature-description">
                    <p class="bullet-point">|</p><p>{{description}}</p>
                </div>
            {% endfor %}
            </div>
            <div class="feature-link">
                <a href="{{documentation_link}}" class="documentation-link">Learn more</a>
                <a href="{{demonstration_video_link}}" class="video-link">Watch demonstration video</a>
            </div>
        </div>
        <img src="/img/{{image_filename}}">
	</div>
{%- endmacro %}