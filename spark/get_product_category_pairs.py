def get_product_category_pairs(products_df, categories_df, product_category_df):
    """
  Этот метод на PySpark принимает три DataFrame:
    * products_df: DataFrame с информацией о продуктах.
    * categories_df: DataFrame с информацией о категориях.
    * product_category_df: DataFrame, который связывает продукты и категории.

  Метод возвращает один DataFrame, который содержит:
    * Все пары "Имя продукта - Имя категории".
    * Имена всех продуктов, у которых нет категорий.

  Args:
    products_df: DataFrame с информацией о продуктах.
    categories_df: DataFrame с информацией о категориях.
    product_category_df: DataFrame, который связывает продукты и категории.

  Returns:
    DataFrame с парами продукт-категория и продуктами без категорий.
  """

    # 1. Объединяем DataFrame products_df и product_category_df по имени продукта
    joined_df = products_df.join(product_category_df, on="product_name", how="left")

    # 2. Заполняем null значения в столбце "category_name" пустой строкой
    joined_df = joined_df.fillna({"category_name": ""})

    # 3. Группируем DataFrame по имени продукта
    grouped_df = joined_df.groupby("product_name")

    # 4. Собираем список категорий для каждого продукта
    aggregated_df = grouped_df["category_name"].agg(lambda x: ", ".join(x.dropna()))

    # 5. Добавляем флаг, который показывает, есть ли у продукта категории
    aggregated_df["has_category"] = aggregated_df["category_name"] != ""

    # 6. Разделяем DataFrame на два DataFrame:
    #    * DataFrame с парами продукт-категория
    #    * DataFrame с продуктами без категорий
    products_with_categories_df = aggregated_df[aggregated_df["has_category"]].select("product_name", "category_name")
    products_without_categories_df = aggregated_df[~aggregated_df["has_category"]].select("product_name")

    # 7. Возвращаем DataFrame с парами продукт-категория и продуктами без категорий
    return products_with_categories_df.union(products_without_categories_df)
