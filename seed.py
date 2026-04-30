{% extends 'base.html' %}

{% block container %}
<main style="padding:40px; max-width:600px; margin:auto;">

    <h2>Edit an Existing Book's Details</h2>

    <form method="POST" action="{{ url_for('edit_book_post', book_id=book.bookId) }}">

        <label>Title:</label><br>
        <input type="text" name="title" value="{{ book.title }}" required><br><br>

        <label>Author:</label><br>
        <input type="text" name="author" value="{{ book.author }}"required><br><br>

        <label>ISBN:</label><br>
        <input type="text" name="isbn" value="{{ book.isbn }}"required><br><br>

        <label>Price:</label><br>
        <input type="number" step="0.01" name="price" value="{{ book.price }}"required><br><br>

        <label>Image filename:</label><br>
        <input type="text" name="image" placeholder="example.jpg" value="{{ book.image }}"required><br><br>

        <label>Category:</label><br>
        <select name="categoryId" required>
            {% for cat in categories %}
                <option value="{{ cat.categoryId }}">{{ cat.categoryName }}</option>
            {% endfor %}
        </select><br><br>

        <label>Read now/available now?:</label><br>
        <label class="switch" style="display:block; margin:10px 0;">
            <input type="checkbox" name="readNow" value="1">
            <span class="slider round"></span>
        </label>


        <button type="submit">Confirm changes</button>
        <a href="{{ url_for('read') }}">
            <button type="button">Cancel</button>
        </a>


    </form>

</main>
{% endblock %}
