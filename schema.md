```
Table users {
  user_id uuid [primary key]
  email varchar [unique, not null]
  password varchar [not null]
  is_active boolean
  created_at timestamp
  updated_at timestamp
  deleted_at timestamp
}

Table collection {
  collection_id uuid [primary key]
  user_id uuid 
  collection_name text [not null]
  collection_description text
  collection_settings jsonb
  created_at timestamp
  updated_at timestamp
  deleted_at timestamp
}

Table document {
  document_id uuid [primary key]
  collection_id uuid
  document_name text [not null]
  document_path text
  mime_type varchar
  status varchar
  error_message text
  document_metadata json
  created_at timestamp
  updated_at timestamp
  deleted_at timestamp
}

Table document_chunks {
  chunk_id uuid PK
  document_id uuid 
  chunk_index integer
  content text
  embedding vector(1536)
  metadata jsonb
  embedding_model varchar
  created_at timestamp
}

Table chat {
  chat_id uuid [primary key]
  collection_id uuid
  chat_name text
  created_at timestamp
  updated_at timestamp
  deleted_at timestamp
}

Table messages{
  message_id uuid PK
  chat_id uuid 
  role varchar
  content text
  metadata jsonb
  created_at timestamp
}

Table memory {
  memory_id uuid [primary key]
  chat_id uuid
  memory_type varchar
  content text
  created_at timestamp
  updated_at timestamp
}

Table message_sources{
  id uuid PK
  message_id uuid
  chunk_id uuid
  relevance_score float
}

Ref: users.user_id < collection.user_id
Ref: collection.collection_id < document.collection_id
Ref: document.document_id < document_chunks.document_id
Ref: collection.collection_id < chat.collection_id
Ref: chat.chat_id < memory.chat_id
Ref: "chat"."chat_id" < "messages"."chat_id"
Ref: "messages"."message_id" < "message_sources"."message_id" 
```