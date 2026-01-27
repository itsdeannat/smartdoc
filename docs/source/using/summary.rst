====================
Generating a summary
====================

To help you get a quick summary of an API's functionality, endpoints, and schemas, you can use the ``summarize`` command. The output is returned in an concise, readable list. It has one required option, ``[file]``.

Example usage
-------------

.. code-block:: bash

    smartdoc summarize sample_oas.json

.. code-block:: text
    :class: wrap-code

    Brew Ha Ha API — quick summary

    Base URL
    - https://api.brewhaha.example.com

    Purpose
    - Place and manage orders for bagged coffee and baked goods.

    Endpoints
    - POST /orders
    - Create a new order.
    - Request body: NewOrder (items: array of { productId, quantity }).
    - Responses: 201 (Order), 400 (Bad request).

    - GET /orders/{orderId}
    - Retrieve an order's status.
    - Path parameter: orderId (string).
    - Responses: 200 (OrderStatus), 404 (Order not found).

    - DELETE /orders/{orderId}
    - Cancel/delete an order.
    - Path parameter: orderId (string).
    - Responses: 204 (Order canceled), 404 (Order not found).

    Key schemas
    - NewOrder: { items: [{ productId: string, quantity: integer ≥1 }] }
    - Order: { orderId: string, items: [OrderItem], status: string }
    - OrderItem: { productId: string, quantity: integer }
    - OrderStatus: { orderId: string, status: string }

    Notes
    - Required fields: NewOrder.items, Order.orderId, Order.status.
