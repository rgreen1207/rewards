
# receipt-processor-challenge




## API Reference

#### Process new receipt

```http
  POST /receipts/process
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `ReceiptPOSTModel` | `JSON` | `localhost:8080/docs` for model information |

#### Get receipt

```http
  GET /receipts/${id}
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `id`      | `uuid` | **Required**. Id of receipt to fetch |

#### Get receipt points

```http
  GET /receipts/${id}/points
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `id`      | `uuid` | **Required**. Id of receipt to fetch points |



## Running Tests

To run tests:

```bash
  pytest
```


## Tech Stack

**Language:** Python3.11

**Framework:** FastAPI

**Database:** A JSON object with dreams
