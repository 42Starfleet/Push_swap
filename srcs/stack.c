/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   stack.c                                            :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: ztisnes <ztisnes@student.42.fr>            +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2018/01/09 19:57:20 by ztisnes           #+#    #+#             */
/*   Updated: 2018/02/03 17:48:15 by ztisnes          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

/*
** Stacks are abstract data structures which helps in the order of elements with
** popping (removing) and pushing (inserting) elements Stacks are just arrays
**
*/
typedef struct		s_stack
{
	struct s_list	*top;
}					t_stack;

t_stack				*init_stack(void)
{
	t_stack			*node;
	node = (t_stack *)malloc(sizeof(t_stack));
	node->top = NULL;
	return (node);
}

void				push_stack(t_stack *stack, void *content)
{
	t_list			*node;

	node = (t_list *)malloc(sizeof(t_list));
	node->content = content;
	node->next = stack->top;
	stack->top = node;
}

void				*pop_stack(t_stack *stack)
{
	t_list			*next;
	void			*anything;

	if (stack->top == NULL)
		return (NULL);
	next = stack->top->next;
	anything = stack->top->content;
	free(stack->top);
	stack->top = next;
	return (anything);
}

void				*peek_stack(t_stack *stack)
{
	if (stack->top == NULL)
		return (NULL);
	return (stack->top->content);
}

int					isEmpty_stack(t_stack *stack)
{
	return (stack->top == NULL);
}
