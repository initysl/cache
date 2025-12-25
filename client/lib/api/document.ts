import { apiClient } from './api';
import {
  DocumentResponse,
  UpdateRequest,
  DeleteBatchRequest,
  StatsResponse,
} from '@/types';

export const documentApi = {
  getById: async (id: string): Promise<DocumentResponse> => {
    try {
      const response = await apiClient.get<DocumentResponse>(
        `/documents/${id}`
      );
      return response.data;
    } catch (error) {
      console.error('Failed to fetch document by ID:', error);
      throw error;
    }
  },

  update: async (
    id: string,
    payload: UpdateRequest
  ): Promise<DocumentResponse> => {
    try {
      const response = await apiClient.put<DocumentResponse>(
        `/documents/${id}`,
        payload
      );
      return response.data;
    } catch (error) {
      console.error('Failed to update document:', error);
      throw error;
    }
  },

  delete: async (id: string): Promise<void> => {
    try {
      await apiClient.delete(`/documents/${id}`);
    } catch (error) {
      console.error('Failed to delete document:', error);
      throw error;
    }
  },

  deleteBatch: async (payload: DeleteBatchRequest): Promise<void> => {
    try {
      await apiClient.post('/batch/delete', payload);
    } catch (error) {
      console.error('Failed to delete documents batch:', error);
      throw error;
    }
  },

  stats: async (): Promise<StatsResponse> => {
    try {
      const response = await apiClient.get<StatsResponse>('/documents/stats');
      return response.data;
    } catch (error) {
      console.error('Failed to fetch document stats:', error);
      throw error;
    }
  },

  clear: async (): Promise<void> => {
    try {
      await apiClient.delete('/documents/clear/all');
    } catch (error) {
      console.error('Failed to clear documents:', error);
      throw error;
    }
  },
};
